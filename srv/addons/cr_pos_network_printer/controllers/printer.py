import time
from odoo import http
from escpos.printer import Network
from PIL import Image
from io import BytesIO
import base64
import threading
import logging
import socket
_logger = logging.getLogger(__name__)

cr_printer_is_busy = False
cr_printers = {}


class KeepAliveNetworkPrinter:
    def __init__(self, host, port=9100, timeout=None, keep_alive_interval=300):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.keep_alive_interval = keep_alive_interval
        self.printer = Network(self.host, self.port, self.timeout)
        self.keep_alive_thread = threading.Thread(target=self.keep_alive, daemon=True)
        self.keep_alive_thread.start()

    def keep_alive(self):
        while True:
            try:
                self.printer._raw(b'\x00')  # Send a null byte or any minimal command
            except Exception as e:
                print(f"Keep-alive failed: {e}. Reconnecting...")
                self.reconnect()
            time.sleep(self.keep_alive_interval)

    def reconnect(self):
        self.printer.close()
        self.printer = Network(self.host, self.port, self.timeout)

    def print_text(self, text):
        try:
            self.printer.text(text)
            self.printer.cut()
        except (BrokenPipeError, socket.error) as e:
            print(f"Error: {e}. Reconnecting and retrying...")
            self.reconnect()
            self.printer.text(text)
            self.printer.cut()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def image(self, image):
        try:
            self.printer.image(image)
            self.printer.cut()
        except (BrokenPipeError, socket.error) as e:
            print(f"Error: {e}. Reconnecting and retrying...")
            self.reconnect()
            self.printer.image(image)
            self.printer.print_and_feed(6)
            self.printer.cut()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


class CrPrinterController(http.Controller):
    @http.route('/cr_print_receipt', type='json', auth='none', cors='*')
    def cr_print_receipt(self, receipt, retry=True):
        global cr_printer_is_busy, cr_printers
        if cr_printer_is_busy:
            time.sleep(2)
            return self.cr_print_receipt(receipt)

        cr_printer_is_busy = True
        _logger.info('Preparing Image...')
        raw_image = receipt['img']
        image = Image.open(BytesIO(base64.b64decode(raw_image)))
        try:
            _logger.info('Connecting To Pinter...')
            if cr_printers.get(receipt['ip']) and retry:
                printer = cr_printers.get(receipt['ip'])
            else:
                printer = KeepAliveNetworkPrinter(receipt['ip'], receipt['port'], None)
                cr_printers[receipt['ip']] = printer
            _logger.info('Printer Connected...\nPrinting Image...')
            printer.image(image)
            # printer.cut()
            _logger.info('Print Job Done.')
        except:
            _logger.exception('Error while printing receipt')
            if not retry:
                _logger.info('Retrying...')
                return self.cr_print_receipt(receipt, False)
            else:
                return False

        cr_printer_is_busy = False
        return True
