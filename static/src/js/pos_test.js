/** @odoo-module */
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { Component } from "@odoo/owl";
import { useState } from "@odoo/owl";

class TestButton extends Component {
    static template = "TestButton";
    setup() {
        this.state = useState({ value: 0 });
    }

    incrementValue(){
        this.state.value++;
        if (this.state.value > 10) {
            this.state.value = 0;
        }
        console.log("Value: ", this.state.value);
    }
    
    resetValue(){
        this.state.value = 0;
    }

}

ProductScreen.addControlButton({
    component: TestButton,
    position: ["before", "RefundButton"],
});
