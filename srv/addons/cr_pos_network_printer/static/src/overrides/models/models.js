/** @odoo-module */

import { PosStore } from "@point_of_sale/app/store/pos_store";
import { CrPrinter } from "@cr_pos_network_printer/app/printers";
import { patch } from "@web/core/utils/patch";

patch(PosStore.prototype, {
    after_load_server_data() {
        var self = this;        
        return super.after_load_server_data(...arguments).then(function () {
            console.log('11',);
            
            if (self.config.other_devices && self.config.cr_network_printer_ip && self.config.cr_network_printer_port) {
                console.log('12',);
                
                self.hardwareProxy.printer = new CrPrinter({rpc:self.env.services.rpc, ip: self.config.cr_network_printer_ip ,port : self.config.cr_network_printer_port});
            }
        });
    }
});
