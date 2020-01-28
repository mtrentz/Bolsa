import smtplib
import html
import mimetypes
from email.headerregistry import Address
import imghdr
from email.utils import make_msgid
from pathlib import Path
import os
from email.message import EmailMessage
import base64
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(to_mail, positive, negative):
    # Email Info
    email_address = 'tz.bolsa@gmail.com'
    email_password = 'v4it3fud3'

    msg = MIMEMultipart()
    msg['Subject'] = 'Suas Ações!'
    msg['From'] = email_address
    msg['to'] = to_mail

    msg_content = MIMEText('Problemas na visualização?', 'plain', 'utf-8')
    msg.attach(MIMEText('''\
<!doctype html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">

<head>
  <title> Discount Light </title>
  <!--[if !mso]><!-- -->
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <!--<![endif]-->
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style type="text/css">
    #outlook a {
      padding: 0;
    }

    body {
      margin: 0;
      padding: 0;
      -webkit-text-size-adjust: 100%;
      -ms-text-size-adjust: 100%;
    }

    table,
    td {
      border-collapse: collapse;
      mso-table-lspace: 0pt;
      mso-table-rspace: 0pt;
    }

    img {
      border: 0;
      height: auto;
      line-height: 100%;
      outline: none;
      text-decoration: none;
      -ms-interpolation-mode: bicubic;
    }

    p {
      display: block;
      margin: 13px 0;
    }
  </style>
  <!--[if mso]>
        <xml>
        <o:OfficeDocumentSettings>
          <o:AllowPNG/>
          <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
        </xml>
        <![endif]-->
  <!--[if lte mso 11]>
        <style type="text/css">
          .mj-outlook-group-fix { width:100% !important; }
        </style>
        <![endif]-->
  <style type="text/css">
    @media only screen and (min-width:480px) {
      .mj-column-per-100 {
        width: 100% !important;
        max-width: 100%;
      }
    }
  </style>
  <style type="text/css">
    @media only screen and (max-width:480px) {
      table.mj-full-width-mobile {
        width: 100% !important;
      }
      td.mj-full-width-mobile {
        width: auto !important;
      }
    }
  </style>
</head>

<body style="background-color:#071e3d;">
  <div style="display:none;font-size:1px;color:#ffffff;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;"> Pre-header Text </div>
  <div style="background-color:#071e3d;">
    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#071e3d;background-color:#071e3d;width:100%;">
      <tbody>
        <tr>
          <td>
            <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->
            <div style="margin:0px auto;max-width:600px;">
              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                <tbody>
                  <tr>
                    <td style="direction:ltr;font-size:0px;padding:20px 0;padding-bottom:0;text-align:center;">
                      <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->
                      <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                          <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                              <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                                <tbody>
                                  <tr>
                                    <td style="width:90px;"> <img alt="" height="auto" src="https://i.imgur.com/L2Wjn7N.png" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;" width="90"> </td>
                                  </tr>
                                </tbody>
                              </table>
                            </td>
                          </tr>
                          <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;padding-top:30px;word-break:break-word;">
                              <div style="font-family:'Helvetica Neue', Helvetica, Arial, sans-serif;font-size:25px;font-weight:bold;letter-spacing:1px;line-height:24px;text-align:center;text-transform:uppercase;color:#ffffff;">Rentabilidade de suas Ações <br></div>
                            </td>
                          </tr>
                          <tr>
                            <td align="center" style="font-size:0px;padding:0;padding-right:30px;word-break:break-word;">
                              <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                                <tbody>
                                  <tr>
                                    <td style="width:570px;"> <img alt="" height="auto" src="cid:0" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;" width="570"> </td>
                                  </tr>
                                </tbody>
                              </table>
                            </td>
                          </tr>
                          <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;padding-top:30px;word-break:break-word;">
                              <div style="font-family:'Helvetica Neue', Helvetica, Arial, sans-serif;font-size:15px;font-weight:bold;letter-spacing:1px;line-height:24px;text-align:center;text-transform:uppercase;color:#ffffff;">Seu portfolio atualizado <br></div>
                            </td>
                          </tr>
                          <tr>
                            <td align="center" style="font-size:0px;padding:0;padding-right:0px;word-break:break-word;">
                              <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                                <tbody>
                                  <tr>
                                    <td style="width:600px;"> <img alt="" height="auto" src="cid:1" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;" width="600"> </td>
                                  </tr>
                                </tbody>
                              </table>
                            </td>
                          </tr>
                          <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;padding-top:30px;word-break:break-word;">
                              <div style="font-family:'Helvetica Neue', Helvetica, Arial, sans-serif;font-size:25px;font-weight:bold;letter-spacing:1px;line-height:24px;text-align:center;text-transform:uppercase;color:#ffffff;">As que mais variaram <br></div>
                            </td>
                          </tr>
                          <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;padding-top:30px;word-break:break-word;">
                              <div style="font-family:'Helvetica Neue', Helvetica, Arial, sans-serif;font-size:15px;font-weight:bold;letter-spacing:1px;line-height:24px;text-align:center;text-transform:uppercase;color:#ffffff;">A que mais subiu de preço foi <br></div>
                            </td>
                          </tr>
                          <tr>
                            <td align="center" style="font-size:0px;padding:0;padding-right:30px;word-break:break-word;">
                              <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                                <tbody>
                                  <tr>
                                    <td style="width:570px;"> <img alt="" height="auto" src="cid:2" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;" width="570"> </td>
                                  </tr>
                                </tbody>
                              </table>
                            </td>
                          </tr>
                          <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;padding-top:30px;word-break:break-word;">
                              <div style="font-family:'Helvetica Neue', Helvetica, Arial, sans-serif;font-size:15px;font-weight:bold;letter-spacing:1px;line-height:24px;text-align:center;text-transform:uppercase;color:#ffffff;">A que mais caiu de preço foi <br></div>
                            </td>
                          </tr>
                          <tr>
                            <td align="center" style="font-size:0px;padding:0;padding-right:30px;word-break:break-word;">
                              <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                                <tbody>
                                  <tr>
                                    <td style="width:570px;"> <img alt="" height="auto" src="cid:3" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;" width="570"> </td>
                                  </tr>
                                </tbody>
                              </table>
                            </td>
                          </tr>
                        </table>
                      </div>
                      <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
            <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      <![endif]-->
          </td>
        </tr>
      </tbody>
    </table>
    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
      <tbody>
        <tr>
          <td>
            <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->
            <div style="margin:0px auto;max-width:600px;">
              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                <tbody>
                  <tr>
                    <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
                      <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
            <tr>
              <td
                 class="" width="600px"
              >
          
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->
                      <div style="margin:0px auto;max-width:600px;">
                        <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                          <tbody>
                            <tr>
                              <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
                                <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->
                                <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                  <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">
                                    <tbody>
                                      <tr>
                                        <td style="vertical-align:top;padding:0;">
                                          <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="" width="100%">
                                            <tr>
                                              <td align="center" style="font-size:0px;padding:0;word-break:break-word;">
                                                <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" role="presentation"
      >
        <tr>
      
              <td>
            <![endif]-->
                                                <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="float:none;display:inline-table;">
                                                  <tr>
                                                    <td style="padding:4px;">
                                                      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#071e3d;border-radius:3px;width:30px;">
                                                        <tr>
                                                          <td style="font-size:0;height:30px;vertical-align:middle;width:30px;"> <a href="https://www.facebook.com/sharer/sharer.php?u=https://mjml.io/" target="_blank">
                    <img height="30" src="https://www.mailjet.com/images/theme/v1/icons/ico-social/facebook.png" style="border-radius:3px;display:block;" width="30">
                  </a> </td>
                                                        </tr>
                                                      </table>
                                                    </td>
                                                  </tr>
                                                </table>
                                                <!--[if mso | IE]>
              </td>
            
              <td>
            <![endif]-->
                                                <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="float:none;display:inline-table;">
                                                  <tr>
                                                    <td style="padding:4px;">
                                                      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#071e3d;border-radius:3px;width:30px;">
                                                        <tr>
                                                          <td style="font-size:0;height:30px;vertical-align:middle;width:30px;"> <a href="https://plus.google.com/share?url=https://mjml.io/" target="_blank">
                    <img height="30" src="https://www.mailjet.com/images/theme/v1/icons/ico-social/google-plus.png" style="border-radius:3px;display:block;" width="30">
                  </a> </td>
                                                        </tr>
                                                      </table>
                                                    </td>
                                                  </tr>
                                                </table>
                                                <!--[if mso | IE]>
              </td>
            
              <td>
            <![endif]-->
                                                <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="float:none;display:inline-table;">
                                                  <tr>
                                                    <td style="padding:4px;">
                                                      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#071e3d;border-radius:3px;width:30px;">
                                                        <tr>
                                                          <td style="font-size:0;height:30px;vertical-align:middle;width:30px;"> <a href="https://twitter.com/home?status=https://mjml.io/" target="_blank">
                    <img height="30" src="https://www.mailjet.com/images/theme/v1/icons/ico-social/twitter.png" style="border-radius:3px;display:block;" width="30">
                  </a> </td>
                                                        </tr>
                                                      </table>
                                                    </td>
                                                  </tr>
                                                </table>
                                                <!--[if mso | IE]>
              </td>
            
              <td>
            <![endif]-->
                                                <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="float:none;display:inline-table;">
                                                  <tr>
                                                    <td style="padding:4px;">
                                                      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#071e3d;border-radius:3px;width:30px;">
                                                        <tr>
                                                          <td style="font-size:0;height:30px;vertical-align:middle;width:30px;"> <a href="https://www.linkedin.com/shareArticle?mini=true&url=https://mjml.io/&title=&summary=&source=" target="_blank">
                    <img height="30" src="https://www.mailjet.com/images/theme/v1/icons/ico-social/linkedin.png" style="border-radius:3px;display:block;" width="30">
                  </a> </td>
                                                        </tr>
                                                      </table>
                                                    </td>
                                                  </tr>
                                                </table>
                                                <!--[if mso | IE]>
              </td>
            
          </tr>
        </table>
      <![endif]-->
                                              </td>
                                            </tr>
                                            <tr>
                                              <td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                                <div style="font-family:'Helvetica Neue', Helvetica, Arial, sans-serif;font-size:11px;font-weight:bold;line-height:24px;text-align:center;color:#445566;">View this email in your browser</div>
                                              </td>
                                            </tr>
                                            <tr>
                                              <td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                                <div style="font-family:'Helvetica Neue', Helvetica, Arial, sans-serif;font-size:11px;font-weight:400;line-height:16px;text-align:center;color:#445566;">You are receiving this email advertisement because you registered with Croft's Accountants. (123 Main Street, Austin, TX 78701) and agreed to receive emails from us regarding new features, events and special
                                                  offers.</div>
                                              </td>
                                            </tr>
                                            <tr>
                                              <td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                                <div style="font-family:'Helvetica Neue', Helvetica, Arial, sans-serif;font-size:11px;font-weight:400;line-height:16px;text-align:center;color:#445566;">&copy; Croft's Accountants Inc., All Rights Reserved.</div>
                                              </td>
                                            </tr>
                                          </table>
                                        </td>
                                      </tr>
                                    </tbody>
                                  </table>
                                </div>
                                <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                      <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      
              </td>
            </tr>
          
            <tr>
              <td
                 class="" width="600px"
              >
          
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->
                      <div style="margin:0px auto;max-width:600px;">
                        <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                          <tbody>
                            <tr>
                              <td style="direction:ltr;font-size:0px;padding:20px 0;padding-top:0;text-align:center;">
                                <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               class="" style="width:600px;"
            >
          <![endif]-->
                                <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0;line-height:0;text-align:left;display:inline-block;width:100%;direction:ltr;">
                                  <!--[if mso | IE]>
        <table  role="presentation" border="0" cellpadding="0" cellspacing="0">
          <tr>
        
              <td
                 style="vertical-align:top;width:600px;"
              >
              <![endif]-->
                                  <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                    <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">
                                      <tbody>
                                        <tr>
                                          <td style="vertical-align:top;padding-right:0;">
                                            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="" width="100%">
                                              <tr>
                                                <td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                                  <div style="font-family:'Helvetica Neue', Helvetica, Arial, sans-serif;font-size:11px;font-weight:bold;line-height:16px;text-align:center;color:#445566;"><a class="footer-link" href="https://www.google.com" style="color: #888888;">Privacy</a>&#xA0;&#xA0;&#xA0;&#xA0;&#xA0;&#xA0;&#xA0;&#xA0;<a class="footer-link" href="https://www.google.com" style="color: #888888;">Unsubscribe</a></div>
                                                </td>
                                              </tr>
                                            </table>
                                          </td>
                                        </tr>
                                      </tbody>
                                    </table>
                                  </div>
                                  <!--[if mso | IE]>
              </td>
              
          </tr>
          </table>
        <![endif]-->
                                </div>
                                <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                      <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      
              </td>
            </tr>
          
                  </table>
                <![endif]-->
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
            <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      <![endif]-->
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</body>

</html>
    ''', 'html', 'utf-8'))

    # TODO testar com varios attachments, mudar os cid numbers
    imglist = ['rentability.png', 'portfolio.png', f'{positive}.png', f'{negative}.png']
    i = 0
    for img in imglist:
        with open(f'Figures\\{img}', 'rb') as f:
            mime = MIMEBase('image', 'png', filename=f'{img}')
            mime.add_header('Content-Disposition', 'attachment', filename=f'{img}')
            mime.add_header('X-Attachment-Id', f'{i}')
            mime.add_header('Content-ID', f'<{i}>')
            mime.set_payload(f.read())
            encoders.encode_base64(mime)
            msg.attach(mime)
            i += 1

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)


# send_mail('tz.bolsa@gmail.com', 'B3SA3', 'EVEN3')
