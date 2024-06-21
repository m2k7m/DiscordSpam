
# [English](https://github.com/m2k7m/DiscordSpam) | العربية 

# DiscordSpam Self-bot

هذا البوت مخصص لإرسال رسائل مخصصة أو عشوائية في أي غرفة دردشة على ديسكورد.

تمت إضافة خاصية الاشتراك التلقائي في الـ Giveaway.

تمت اضافة ميزة الـ AFK في اي محادثة صوتية بواسطة امر !v و كتابة ايدي الروم الصوتي.
___

## التثبيت

1 - قم بتنزيل المصدر بصيغة ZIP.
2 - استعمل أمر :
```bash
pip install -r requirements.txt
```

* لو كنت تستخدم استضافة فسيثبت لك المكتبات تلقائياز

## التشغيل

قم بتغيير المتغيرات في ملف `config.yml`:

`TOKEN:` ضع توكن حسابك هنا.<br>
`CHANNELID:` غير 123 إلى معرف الغرفة.<br>
`LANGUAGE:` اكتب `ar` للغة العربية و `en` للغة الإنجليزية. لاستخدام الرسائل المخصصة، اكتب `"custom"` هنا.<br>
`TIME:` الوقت بالثواني، 120 يعادل دقيقتين.<br>
`CONTANT:` محتوى الرسائل المخصصة.<br>
`DEL:` قم بتغييرها إلى True ليقوم البوت بحذف الرسالة بعد إرسالها.

## Token 

كيف تحصل على توكن حسابك؟ (يعمل على الهاتف والكمبيوتر)

قم بتسجيل الدخول إلى [ديسكورد](https://discord.com/login)، ثم الصق هذا الأمر:

```javascript
javascript:(function()%7Blocation.reload()%3Bvar%20i%20%3D%20document.createElement('iframe')%3Bdocument.body.appendChild(i)%3Bdocument.write(i.contentWindow.localStorage.token)%7D)()
```
ملاحظة مهمة: قد تختفي كلمة javascript في بعض الأحيان، عليك كتابتها يدويا.

## استضافة

هنا بعض المواقع التي يمكنك من خلالها استضافة بوت Discord الخاص بك مجانًا:

1. [FPS.MS](https://panel.fps.ms/auth/login)
2. [Bot-Hosting.net](https://bot-hosting.net/?aff=1203278055229882418)
3. [PylexNodes.net](https://client.pylexnodes.net/dashboard)

