/** @odoo-module **/
import {Markup} from "web.utils";
import {browser} from "@web/core/browser/browser";
import {registry} from "@web/core/registry";

export const webNotificationService = {
    dependencies: ["bus_service", "notification"],

    start(env, {bus_service, notification}) {
        let webNotifTimeouts = {};
        /**
         * Displays the web notification on user's screen
         */

        function displaywebNotification(notifications) {
            Object.values(webNotifTimeouts).forEach((notif) =>
                browser.clearTimeout(notif)
            );
            webNotifTimeouts = {};

            notifications.forEach(function (notif) {
                browser.setTimeout(function () {
                    notification.add(Markup(notif.message), {
                        title: notif.title,
                        type: notif.type,
                        sticky: notif.sticky,
                        className: notif.className,
                    });
                });
            });
        }

        bus_service.addEventListener("notification", ({detail: notifications}) => {
            for (const {payload, type} of notifications) {
                if (type === "web.notify") {
                    // console.log("play")
                    var audio = new Audio('/web_sale_order_sound_notify/static/src/js/services/Notification_Sound.mp3');
                    audio.play();                    
                    displaywebNotification(payload);
                    }
            }
        });
        bus_service.start();
    },
};

registry.category("services").add("webNotification", webNotificationService);
