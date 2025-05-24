/* @odoo-module */

import { BasePrinter } from "@point_of_sale/app/printer/base_printer";

export class CrPrinter extends BasePrinter {
    setup({rpc, ip ,port}) {
        super.setup(...arguments);
        this.rpc = rpc;
        this.ip = ip;
        this.port = port;
        
    }

    async sendPrintingJob(img) {
        if (!this.ip) {            
            return false
        }
        let receipt = {
            'ip': this.ip,
            'port': parseInt(this.port) || 9100,
            'img': img
        }        
        let result;
        await this.rpc(
            '/cr_print_receipt',{
            receipt 
        }).then(function (res) {
            result = res;
        }).catch(function (err) {
            console.error(err);
            result = false;
        });

        return { result ,printerErrorCode: false};
    }
}
