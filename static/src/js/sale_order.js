/** @odoo-module */

import { ListController } from "@web/views/list/list_controller";
import { registry } from '@web/core/registry';
import { listView } from '@web/views/list/list_view';

export class OdooOwlListController extends ListController {
    setup() {
        super.setup();
    }

    showCustomers() {
        this.actionService.doAction({
            type: 'ir.actions.act_window',
            res_model: 'res.partner',
            name:'Customers',
            view_mode: 'tree,form',
            view_type: 'form',
            views: [[false, 'tree'], [false, 'form']],
            target: 'current',
            res_id: false,
            // context: { "readonly": true },
        });
    }
}

export class TestListener extends ListController {
    setup() {
        super.setup();
    }

    showCustomers() {
        this.actionService.doAction({
            type: 'ir.actions.act_window',
            res_model: 'product.template',
            name:'Product',
            view_mode: 'kanban, form',
            // view_type: 'kanban',
            views: [[false, 'kanban'], [false, 'form']],
            target: 'current',
            res_id: false,
            context: { "readonly_by_form": true },
        });
    }
}
// registry.category("views").add("test_list_controller", TestListener);

const viewRegistry = registry.category("views");
// export const OwlListController = {
//     ...listView,
//     Controller: OdooOwlListController,
// };
export const TestController = {
    ...listView,
    Controller: TestListener,
};
// viewRegistry.add("owl_list_controller", OwlListController);
viewRegistry.add("test_list_controller", TestController);