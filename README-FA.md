🎮 بازی UNO – پیاده‌سازی با پایتون

این پروژه یک پیاده‌سازی کامل از بازی UNO با زبان Python است که شامل:

نسخه ترمینالی (CLI)

و یک نسخه گرافیکی آزمایشی (GUI)

طراحی پروژه روی خوانایی کد، معماری تمیز و قابل توسعه بودن تمرکز دارد.

✨ قابلیت‌ها

🎴 پیاده‌سازی کامل قوانین UNO

👥 پشتیبانی از چند بازیکن (انسان و کامپیوتر)

🤖 هوش مصنوعی ساده برای بازیکن کامپیوتری

🧠 قانون اختیاری Stack کردن کارت‌ها

🎨 انتخاب رنگ برای کارت‌های Wild

🖥 رابط ترمینالی حرفه‌ای با rich

🌐 رابط گرافیکی (HTML + React)

⚙️ طراحی ماژولار و شی‌گرا

🗂 ساختار پروژه
main.py        منطق اصلی اجرای بازی
game.py        قوانین و منطق UNO
enums.py       enumهای کارت، رنگ و رویداد
exceptions.py  خطاهای سفارشی
uno-gui.html   نسخه گرافیکی آزمایشی

🚀 اجرای بازی (نسخه ترمینال)
پیش‌نیازها

Python نسخه 3.9 یا بالاتر

کتابخانه rich

pip install rich
python main.py

🎮 پارامترهای اجرا
گزینه	توضیح
--cheats	فعال‌سازی کدهای تقلب
--debug	نمایش لاگ‌های دیباگ
--version	نمایش نسخه
🧠 نکات گیم‌پلی

کارت Wild و +4 نیاز به انتخاب رنگ دارند

Reverse در بازی ۲ نفره مثل Skip عمل می‌کند

+2 و +4 فوراً اعمال می‌شوند

امکان Stack کارت‌های مشابه (اختیاری)

هوش مصنوعی رنگ منطقی را انتخاب می‌کند

🖥 نسخه گرافیکی (GUI)

فایل uno-gui.html شامل نسخه گرافیکی بازی است.

برای اجرا:

فایل را مستقیماً در مرورگر باز کنید

⚠️ این نسخه فعلاً مستقل از موتور Python اجرا می‌شود.

🧪 کدهای تقلب (Cheats)

در صورت فعال بودن:

#<کد پایتون>


مثال:

#game.turn.hand.clear()


برای تست، دیباگ و شیطنت علمی 😄

📌 نسخه
ALPHA-2025-06-02

📜 مجوز

این پروژه صرفاً آموزشی و آزمایشی است.
UNO یک علامت تجاری متعلق به Mattel می‌باشد.

🌱 ایده‌های توسعه آینده

مولتی‌پلیر آنلاین

اتصال GUI به موتور Python

AI پیشرفته‌تر

تست خودکار (Unit Tests)

ذخیره وضعیت بازی

اگر بخوای، می‌تونم:

README رو دانشجویی / شرکتی / رزومه‌ای کنم

نسخه مخصوص GitHub با badge و screenshot بسازم

یا حتی مستندات فنی (Technical Docs) براش بنویسم

این پروژه از اوناییه که می‌تونه تو رزومه بدرخشه، فقط باید درست ارائه بشه ✨

هم فارسی هم اینگلیسی نسخه git hub بساز

عالی. این پایین نسخه مخصوص GitHub رو می‌گیری:
تمیز، حرفه‌ای، دوزبانه، با ساختار استاندارد ریپازیتوری‌های جدی.
می‌تونی عیناً کپی کنی بذاری تو README.md 👇

🎮 UNO Game – Python Implementation








A clean and extensible implementation of the UNO card game written in Python, featuring a powerful CLI engine and an experimental GUI (React).
Designed with readability, modularity, and correctness in mind.

✨ Features

🎴 Full UNO rules implementation

👥 Multiplayer support (Human & Computer)

🤖 Basic AI for computer players

🧠 Optional card stacking rule

🎨 Wildcard color selection

🖥 Rich terminal interface (rich)

🌐 Experimental graphical UI (HTML + React)

⚙️ Object-Oriented & modular design

🗂 Project Structure
.
├── main.py           # CLI entry point
├── game.py           # Core game logic
├── enums.py          # Enums (cards, colors, events)
├── exceptions.py     # Custom exceptions
├── uno-gui.html      # Experimental GUI (React)
└── README.md

🚀 Getting Started (CLI)
Requirements

Python 3.9+

rich library

pip install rich
python main.py

🎮 Command-Line Options
Option	Description
-C, --cheats	Enable cheat codes
-D, --debug	Enable debug logging
-V, --version	Show version and exit
🧠 Gameplay Details

Wildcard and +4 require color selection

Reverse behaves correctly in 2-player games

Skip / +2 / +4 effects apply immediately

Optional stacking of similar card types

AI selects the most reasonable color automatically

🖥 GUI Version (Experimental)

The file uno-gui.html contains a standalone React-based GUI.

Open directly in a browser:

uno-gui.html


⚠️ The GUI currently runs independently and is not connected to the Python game engine.

🧪 Cheat Codes (CLI)

When cheats are enabled:

#<python-code>


Example:

#game.turn.hand.clear()

📌 Version
ALPHA-2025-06-02

📜 License

This project is intended for educational and experimental use.
UNO is a trademark of Mattel — this is a fan-made implementation.

🌱 Future Improvements

Online multiplayer

Unified engine for CLI & GUI

Smarter AI strategies

Automated testing

Persistent game state

🎮 بازی UNO – پیاده‌سازی با پایتون






این پروژه یک پیاده‌سازی حرفه‌ای و ماژولار از بازی UNO با زبان Python است که شامل:

نسخه ترمینالی (CLI)

نسخه گرافیکی آزمایشی (GUI)

تمرکز اصلی روی خوانایی کد، طراحی شی‌گرا و توسعه‌پذیری بوده است.

✨ قابلیت‌ها

🎴 پیاده‌سازی کامل قوانین UNO

👥 چندبازیکنه (انسان و کامپیوتر)

🤖 هوش مصنوعی ساده

🧠 قانون اختیاری Stack کارت‌ها

🎨 انتخاب رنگ برای Wild

🖥 رابط ترمینال حرفه‌ای

🌐 رابط گرافیکی با React

⚙️ معماری تمیز و قابل توسعه

🗂 ساختار پروژه
main.py        نقطه شروع بازی
game.py        منطق اصلی و قوانین
enums.py       enumهای کارت و رویداد
exceptions.py  مدیریت خطاها
uno-gui.html   رابط گرافیکی

🚀 اجرای بازی (CLI)
پیش‌نیازها

Python 3.9+

کتابخانه rich

pip install rich
python main.py

🎮 تنظیمات اجرا
گزینه	توضیح
--cheats	فعال‌سازی کد تقلب
--debug	نمایش لاگ دیباگ
--version	نمایش نسخه
🧠 منطق بازی

Wild و +4 نیاز به انتخاب رنگ دارند

Reverse در بازی دو نفره مثل Skip عمل می‌کند

+2 و +4 بلافاصله اعمال می‌شوند

امکان Stack کارت‌های مشابه

AI رنگ منطقی را انتخاب می‌کند

🖥 نسخه گرافیکی

فایل uno-gui.html را مستقیماً در مرورگر باز کنید.

⚠️ این نسخه فعلاً به موتور Python متصل نیست.

🧪 کد تقلب

در صورت فعال بودن Cheats:

#<کد پایتون>


مثال:

#game.turn.hand.clear()

📌 نسخه
ALPHA-2025-06-02

📜 مجوز

این پروژه صرفاً آموزشی و آزمایشی است.
حقوق برند UNO متعلق به Mattel می‌باشد.

🌱 برنامه‌های آینده

مولتی‌پلیر آنلاین

اتصال GUI به موتور اصلی

هوش مصنوعی پیشرفته

تست خودکار

ذخیره وضعیت بازی
