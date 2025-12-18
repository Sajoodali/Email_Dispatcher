import base64

def get_email_template(message_body, company_name, company_address, company_website, logo_base64=None):
    # Set defaults if values are empty
    display_company_name = company_name if company_name else "Globium Cloud"
    display_address = company_address if company_address else "Official Business Address"
    display_website = company_website if company_website else "www.globiumcloud.com"
    
    # Logo HTML with refined white badge
    logo_html = ""
    if logo_base64:
        logo_html = f"""
        <div style="background: #ffffff; width: 80px; height: 80px; border-radius: 50%; 
                    margin: 0 auto 20px auto; display: block; box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                    text-align: center;">
            <table width="100%" height="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                    <td align="center" valign="middle">
                        <img src="data:image/jpeg;base64,{logo_base64}" alt="{display_company_name} Logo" 
                             style="width: 55px; height: auto; display: block; border-radius: 5px;">
                    </td>
                </tr>
            </table>
        </div>
        """
    else:
        logo_html = f'<div style="font-size: 32px; font-weight: 900; color: white; margin-bottom: 10px;">{display_company_name[0]}</div>'

    html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Official Communication | {display_company_name}</title>
    <style>
        /* Reset styles for email clients */
        body, table, td, a {{ -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }}
        table, td {{ mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-collapse: collapse !important; }}
        img {{ border: 0; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; }}
        
        /* Mobile Adjustments */
        @media only screen and (max-width: 620px) {{
            .wrapper-table {{ padding: 0 !important; }}
            .main-card {{ width: 100% !important; border-radius: 0 !important; border: none !important; }}
            .message-body {{ padding: 35px 25px !important; }}
            .header-td {{ padding: 40px 20px !important; }}
            .brand-name {{ font-size: 24px !important; }}
        }}
    </style>
</head>
<body style="margin: 0; padding: 0; width: 100% !important; height: 100% !important; background-color: #f1f5f9; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
    <center style="width: 100%; background-color: #f1f5f9;">
        <table width="100%" border="0" cellpadding="0" cellspacing="0" bgcolor="#f1f5f9" style="width: 100%; background-color: #f1f5f9;">
            <tr>
                <td align="center" valign="top" class="wrapper-table" style="padding: 40px 0;">
                    <!-- Main Card -->
                    <table class="main-card" width="600" border="0" cellpadding="0" cellspacing="0" bgcolor="#ffffff" style="width: 600px; max-width: 600px; background-color: #ffffff; border-radius: 24px; overflow: hidden; box-shadow: 0 10px 40px rgba(0,0,0,0.04); border: 1px solid #e2e8f0;">
                        <!-- Dynamic Header -->
                        <tr>
                            <td class="header-td" align="center" style="background-color: #0077FF; background: linear-gradient(135deg, #00A3FF 0%, #0077FF 100%); padding: 50px 30px;">
                                <!-- Logo Container -->
                                <table width="100%" border="0" cellpadding="0" cellspacing="0">
                                    <tr>
                                        <td align="center">
                                            {logo_html}
                                        </td>
                                    </tr>
                                    <tr>
                                        <td align="center">
                                            <div class="brand-name" style="margin: 0; font-size: 28px; font-weight: 800; letter-spacing: -1px; color: #ffffff; text-transform: uppercase; font-family: sans-serif;">{display_company_name}</div>
                                            <div class="subheader" style="color: rgba(255, 255, 255, 0.85); font-size: 14px; font-weight: 500; margin-top: 8px; letter-spacing: 1px; text-transform: uppercase;">Official Communication</div>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>

                        <!-- Content Area -->
                        <tr>
                            <td class="message-body" style="padding: 50px 40px; color: #1e293b;">
                                <table width="100%" border="0" cellpadding="0" cellspacing="0">
                                    <tr>
                                        <td class="text-content" style="font-size: 17px; line-height: 1.8; color: #334155; white-space: pre-wrap; font-family: sans-serif;">
                                            {message_body}
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="padding-top: 40px; padding-bottom: 40px;">
                                            <table width="100%" border="0" cellpadding="0" cellspacing="0">
                                                <tr>
                                                    <td style="border-bottom: 1px solid #e2e8f0; font-size: 0; line-height: 0;">&nbsp;</td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td align="center">
                                            <a href="http://{display_website}" class="cta-button" style="display: inline-block; background-color: #0077FF; color: #ffffff !important; padding: 14px 28px; border-radius: 12px; text-decoration: none !important; font-weight: 700; font-size: 15px; box-shadow: 0 4px 12px rgba(0, 119, 255, 0.2); font-family: sans-serif;">Visit Official Website</a>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>

                        <!-- Footer Details -->
                        <tr>
                            <td class="footer" align="center" style="background-color: #f8fafc; padding: 40px 30px; border-top: 1px solid #e2e8f0;">
                                <table width="100%" border="0" cellpadding="0" cellspacing="0">
                                    <tr>
                                        <td align="center" class="footer-text" style="color: #64748b; font-size: 14px; margin: 8px 0; line-height: 1.5; font-family: sans-serif;">
                                            <strong>{display_company_name} HQ</strong><br>
                                            {display_address}
                                        </td>
                                    </tr>
                                    <tr>
                                        <td align="center" class="footer-text" style="padding-top: 8px; color: #64748b; font-size: 14px; line-height: 1.5; font-family: sans-serif;">
                                            <a href="http://{display_website}" class="footer-link" style="color: #0077FF; text-decoration: none; font-weight: 600;">{display_website}</a>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td align="center" class="legal-notice" style="font-size: 12px; color: #94a3b8; margin-top: 25px; padding-top: 25px; border-top: 1px solid #eef2f6; font-family: sans-serif;">
                                            <br>
                                            This is an automated message from <b>{display_company_name}</b>.<br>
                                            © 2025 All Rights Reserved.
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </center>
</body>
</html>
    """
    return html_template