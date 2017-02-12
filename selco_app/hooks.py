# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "selco_app"
app_title = "SELCO Customizations"
app_publisher = "Basawaraj Savalagi"
app_description = "This app contains all the customizations of SELCO"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "basawaraj@selco-india.com"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/selco_app/css/selco_app.css"
# app_include_js = "/assets/selco_app/js/selco_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/selco_app/css/selco_app.css"
# web_include_js = "/assets/selco_app/js/selco_app.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "selco_app.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "selco_app.install.before_install"
# after_install = "selco_app.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "selco_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"selco_app.tasks.all"
# 	],
# 	"daily": [
# 		"selco_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"selco_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"selco_app.tasks.weekly"
# 	]
# 	"monthly": [
# 		"selco_app.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "selco_app.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "selco_app.event.get_events"
# }

