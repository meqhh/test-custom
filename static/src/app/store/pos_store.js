/** @odoo-module */
import { useState } from "@odoo/owl";

export function usePosStore() {
    const state = useState({
        is_backspace: false,
    });

    // Define store logic here
    return {
        is_backspace: state.is_backspace,
        loadPosData(data) {
            state.is_backspace = data.config.is_backspace;
        },
    };
}