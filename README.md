# WEB_HW5
утиліта, яка повертає курс EUR та USD ПриватБанку протягом останніх кількох днів. 
В утиліті можна дізнатися курс валют не більше, ніж за останні 10 днів. 
Для запиту до АПІ використовується Aiohttp client. 

Варіанти виклику: 

py main.py             - курс валют за сьогодні

py main.py \<date\> \<days\>  - курс валют за \<days\> днів від дати \<date\> (включно з самою \<date\>)

py main.py \<date\>         - курс валют за вказану дату \<date\> 

py main.py \<days\>         - курс валют за \<days\> днів від поточної дати (включно з сьогодні)
