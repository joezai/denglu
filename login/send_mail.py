import os
#from django.core.mail import send_mail
#
#os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
#
#if __name__ == '__main__':
#
#    send_mail(
#        '来自joe的测试邮件',
#        '欢迎访问joe得网站！',
#        '3178097811@qq.com',
#        ['3178097811@qq.com'],
#    )
import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'denglu.settings'

if __name__ == '__main__':

    subject, from_email, to = '来自joe的测试邮件', '3178097811@qq.com', '3178097811@qq.com'
    text_content = '欢迎访问！'
    html_content = '<p>yoyo切克岛！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()#