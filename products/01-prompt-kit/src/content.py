# -*- coding: utf-8 -*-
# Content for the BSI AI Prompt Kit. Each prompt:
# (title_ar, title_en, when_ar, when_en, prompt_ar, prompt_en, tip_ar, tip_en, saudi_dialect)

SECTIONS = []

def section(key, ar, en, intro_ar, intro_en):
    s = {"key": key, "ar": ar, "en": en, "intro_ar": intro_ar, "intro_en": intro_en, "prompts": []}
    SECTIONS.append(s)
    return s["prompts"]

def P(lst, t_ar, t_en, w_ar, w_en, p_ar, p_en, tip_ar, tip_en, dialect=False):
    lst.append(dict(t_ar=t_ar, t_en=t_en, w_ar=w_ar, w_en=w_en, p_ar=p_ar, p_en=p_en,
                    tip_ar=tip_ar, tip_en=tip_en, dialect=dialect))

# ---------------------------------------------------------------- 1
s = section("marketing", "التسويق ومنشورات التواصل الاجتماعي", "Marketing & Social Media Posts",
            "أوامر لكتابة منشورات إنستغرام وإكس وسناب شات وتيك توك بنبرة تناسب جمهورك في السعودية والخليج.",
            "Prompts for Instagram, X, Snapchat and TikTok content in a tone that fits your Saudi and Gulf audience.")

P(s, "خطة محتوى شهرية", "Monthly Content Plan",
  "في بداية كل شهر عندما تحتاج جدولًا واضحًا لما ستنشره.",
  "At the start of each month, when you need a clear posting schedule.",
  "أنت مدير تسويق رقمي خبير في السوق السعودي. أعدّ خطة محتوى لمدة [عدد الأيام] يومًا لمشروع [اسم المشروع] الذي يقدّم [المنتج أو الخدمة] لجمهور [وصف الجمهور] في [المدينة]. المنصات: [المنصات]. لكل يوم اكتب: المنصة، نوع المحتوى (صورة، فيديو قصير، قصة، نص)، فكرة المنشور في سطر واحد، والهدف (توعية، تفاعل، بيع). وزّع الأفكار بين محتوى تعليمي وترفيهي وترويجي، ولا تجعل المحتوى الترويجي أكثر من ثلثها. قدّم النتيجة في جدول.",
  "You are an expert digital marketing manager for the Saudi market. Build a [NUMBER_OF_DAYS]-day content plan for [BUSINESS_NAME], which offers [PRODUCT_OR_SERVICE] to [AUDIENCE_DESCRIPTION] in [CITY]. Platforms: [PLATFORMS]. For each day give: platform, content type (image, short video, story, text), a one-line post idea, and the goal (awareness, engagement, sales). Mix educational, entertaining and promotional content, keeping promotional posts to no more than one third. Present the result as a table.",
  "اطلب منه بعد ذلك تحويل أي سطر في الجدول إلى منشور كامل، بدل أن تطلب ثلاثين منشورًا دفعة واحدة.",
  "Afterwards, ask it to expand one row at a time into a full post instead of requesting thirty finished posts at once.")

P(s, "منشور إنستغرام مع وسوم", "Instagram Caption with Hashtags",
  "عند نشر صورة منتج أو صورة من داخل المحل.",
  "When posting a product photo or a behind-the-scenes shot.",
  "اكتب 3 نسخ مختلفة لتعليق منشور إنستغرام عن [المنتج أو الخدمة] من [اسم المشروع]. النبرة: [النبرة: ودّية / فاخرة / مرحة]. اكتب باللهجة السعودية البيضاء القريبة من الناس. كل نسخة: سطر أول جذّاب يوقف التمرير، ثم 2–3 أسطر عن الفائدة للعميل، ثم دعوة واضحة لاتخاذ إجراء مثل [الإجراء المطلوب]. أضف 8 وسوم (هاشتاقات) عربية وإنجليزية مناسبة لـ [المدينة] و[المجال]. استخدم رموزًا تعبيرية باعتدال.",
  "Write 3 different Instagram captions for [PRODUCT_OR_SERVICE] from [BUSINESS_NAME]. Tone: [TONE: friendly / premium / playful]. Write in friendly, widely-understood Saudi dialect. Each version: an attention-grabbing first line, then 2–3 lines on the customer benefit, then a clear call to action such as [DESIRED_ACTION]. Add 8 Arabic and English hashtags relevant to [CITY] and [INDUSTRY]. Use emojis sparingly.",
  "انسخ النسخة التي تعجبك واطلب: «اجعلها أقصر بنسبة النصف» — غالبًا ما تكون النسخة الأقصر أقوى.",
  "Take the version you like and ask: \"Make it half as long\" — the shorter version is often stronger.",
  dialect=True)

P(s, "سلسلة تغريدات (ثريد) على إكس", "X (Twitter) Thread",
  "عندما تريد بناء ثقة بمشاركة خبرتك في مجالك.",
  "When you want to build trust by sharing your expertise.",
  "اكتب سلسلة تغريدات (ثريد) من [عدد التغريدات] تغريدات على منصة إكس بعنوان: [موضوع الثريد]. الكاتب صاحب مشروع [نوع المشروع] في السعودية ويريد مشاركة نصائح عملية لجمهور [وصف الجمهور]. التغريدة الأولى خطّاف قوي يدفع للقراءة. كل تغريدة لا تتجاوز 260 حرفًا وتحمل فكرة واحدة. التغريدة الأخيرة تلخّص وتدعو للمتابعة أو زيارة [الرابط أو الحساب]. لا تذكر أرقامًا أو إحصاءات غير مؤكدة.",
  "Write an X thread of [NUMBER_OF_POSTS] posts titled: [THREAD_TOPIC]. The author owns a [BUSINESS_TYPE] in Saudi Arabia and wants to share practical tips with [AUDIENCE_DESCRIPTION]. The first post is a strong hook. Each post is under 260 characters and carries one idea. The last post summarises and invites people to follow or visit [LINK_OR_HANDLE]. Do not include unverified numbers or statistics.",
  "اطلب منه 5 خيارات للتغريدة الأولى وحدها؛ فهي التي تحدد إن كان أحد سيقرأ الباقي.",
  "Ask for 5 alternative opening posts on their own — the first post decides whether anyone reads the rest.")

P(s, "سيناريو فيديو تيك توك / ريلز", "TikTok / Reels Video Script",
  "قبل تصوير فيديو قصير بالجوال.",
  "Before filming a short vertical video on your phone.",
  "اكتب سيناريو فيديو قصير مدته [المدة بالثواني] ثانية لتيك توك وريلز عن [فكرة الفيديو] لمشروع [اسم المشروع]. اكتب الكلام المنطوق باللهجة السعودية. قسّم السيناريو إلى جدول من ثلاثة أعمدة: الثانية، ما يظهر على الشاشة (اللقطة والنص المكتوب)، وما يُقال. أول 3 ثوانٍ يجب أن تشد الانتباه. اختم بدعوة إلى [الإجراء المطلوب]. اقترح أيضًا نصًا قصيرًا للغلاف وتعليقًا للمنشور.",
  "Write a [DURATION_SECONDS]-second TikTok/Reels script about [VIDEO_IDEA] for [BUSINESS_NAME]. Write the spoken lines in Saudi dialect. Format as a three-column table: second, on-screen (shot and text overlay), and voice-over. The first 3 seconds must hook the viewer. End with a call to [DESIRED_ACTION]. Also suggest short cover text and a caption.",
  "صوّر بإضاءة طبيعية قرب نافذة، ولا تحاول قراءة السيناريو حرفيًا — استخدمه كدليل فقط.",
  "Film in natural light near a window, and don't read the script word for word — use it as a guide.",
  dialect=True)

P(s, "أفكار قصص سناب شات ليوم كامل", "A Day of Snapchat Stories",
  "عندما تريد إظهار الجانب الإنساني لمشروعك يوميًا.",
  "When you want to show the human side of your business daily.",
  "اقترح تسلسلًا من [عدد القصص] قصة سناب شات ليوم عمل واحد في [نوع المشروع] اسمه [اسم المشروع]. ابدأ من الصباح حتى الإغلاق. لكل قصة: ما يتم تصويره، نص قصير يُكتب على الشاشة باللهجة السعودية، وهل تحتوي على استفتاء أو سؤال للتفاعل. اجعل قصتين فقط ترويجيتين بشكل مباشر، والباقي يُظهر الكواليس والفريق وطريقة العمل. راعِ الخصوصية ولا تقترح تصوير العملاء.",
  "Suggest a sequence of [NUMBER_OF_STORIES] Snapchat stories for one working day at [BUSINESS_NAME], a [BUSINESS_TYPE]. Go from opening to closing. For each story: what to film, short on-screen text in Saudi dialect, and whether it includes a poll or question. Only two stories should be directly promotional; the rest show behind the scenes, the team and the process. Respect privacy and do not suggest filming customers.",
  "إن ظهر أشخاص في التصوير فاستأذنهم أولًا، خصوصًا في المحلات النسائية والعائلية.",
  "If people appear on camera, get their permission first — especially in family or women-focused venues.",
  dialect=True)

P(s, "إعادة تدوير منشور واحد لكل المنصات", "Repurpose One Post for Every Platform",
  "عندما يكون لديك محتوى جيد وتريد نشره في أكثر من مكان.",
  "When you have one good piece of content and want to use it everywhere.",
  "هذا نص منشور ناجح لدي: [ألصق النص هنا]. حوّله إلى: (1) تعليق إنستغرام مع 6 وسوم، (2) تغريدة على إكس أقل من 260 حرفًا، (3) نص قصة سناب شات من 3 شرائح، (4) فكرة فيديو تيك توك من 20 ثانية، (5) رسالة واتساب قصيرة لقائمة العملاء الذين وافقوا على استلام الرسائل. حافظ على نفس الفكرة الأساسية، وغيّر الأسلوب ليناسب كل منصة.",
  "Here is a post that performed well for me: [PASTE_POST_HERE]. Turn it into: (1) an Instagram caption with 6 hashtags, (2) an X post under 260 characters, (3) a 3-slide Snapchat story text, (4) a 20-second TikTok idea, (5) a short WhatsApp message for customers who opted in to receive messages. Keep the same core idea and adapt the style to each platform.",
  "لا ترسل رسائل واتساب تسويقية إلا لمن وافق على استلامها؛ هذا يحمي سمعتك ورقمك.",
  "Only send marketing WhatsApp messages to people who agreed to receive them — it protects your reputation and your number.")

P(s, "فكرة تصميم لمنشور في Canva", "Canva Post Design Brief",
  "قبل فتح Canva أو استخدام Magic Design.",
  "Before opening Canva or using Magic Design.",
  "أنا أصمم منشورًا في Canva لمشروع [اسم المشروع]. ألوان الهوية: [الألوان]. الرسالة: [الرسالة الأساسية]. اكتب لي: (1) عنوانًا رئيسيًا عربيًا لا يتجاوز 6 كلمات، (2) سطرًا فرعيًا، (3) نص زر أو دعوة للإجراء، (4) وصفًا للتخطيط (أين يوضع النص والصورة)، (5) وصفًا إنجليزيًا قصيرًا يمكنني لصقه في أداة توليد الصور أو Magic Design في Canva، مع مراعاة أن تكون الصور محتشمة ومناسبة للثقافة السعودية.",
  "I'm designing a post in Canva for [BUSINESS_NAME]. Brand colours: [BRAND_COLOURS]. Message: [CORE_MESSAGE]. Give me: (1) an Arabic headline of 6 words or fewer, (2) a sub-line, (3) button / call-to-action text, (4) a layout description (where text and image go), (5) a short English prompt I can paste into Canva's Magic Design or image generator, making sure imagery is modest and culturally appropriate for Saudi Arabia.",
  "تأكد في Canva من أن الخط العربي المختار يدعم الحروف المتصلة، وراجع النص العربي بعد التوليد لأن بعض الأدوات تفصل الحروف.",
  "In Canva, check that your chosen Arabic font connects letters properly, and review Arabic text after generation — some tools break the letters apart.")

P(s, "نص إعلان ممول", "Paid Ad Copy",
  "قبل إطلاق إعلان على سناب شات أو إنستغرام أو إكس.",
  "Before launching a paid ad on Snapchat, Instagram or X.",
  "اكتب 5 نسخ إعلانية قصيرة لإعلان ممول على [المنصة] لمنتج [المنتج أو الخدمة] من [اسم المشروع]. الجمهور المستهدف: [وصف الجمهور] في [المدينة أو المنطقة]. الميزة الأهم: [الميزة]. العرض إن وُجد: [العرض]. لكل نسخة: عنوان أقل من 30 حرفًا، ونص أقل من 90 حرفًا، ونص زر. اجعل كل نسخة تعتمد زاوية مختلفة: السعر، الجودة، السرعة، التجربة، الثقة. لا تستخدم ادعاءات مبالغًا فيها مثل «الأفضل في المملكة».",
  "Write 5 short ad variations for a paid ad on [PLATFORM] for [PRODUCT_OR_SERVICE] from [BUSINESS_NAME]. Target audience: [AUDIENCE_DESCRIPTION] in [CITY_OR_REGION]. Key benefit: [KEY_BENEFIT]. Offer, if any: [OFFER]. For each: a headline under 30 characters, body text under 90 characters, and button text. Give each version a different angle: price, quality, speed, experience, trust. Avoid exaggerated claims such as \"the best in the Kingdom\".",
  "شغّل نسختين أو ثلاثًا بميزانية صغيرة أولًا، ثم ضع ميزانيتك على النسخة التي تحقق نتيجة أفضل فعليًا.",
  "Run two or three versions on a small budget first, then put your money behind the one that actually performs better.")

# ---------------------------------------------------------------- 2
s = section("store", "أوصاف منتجات المتاجر الإلكترونية", "Online Store Product Descriptions",
            "أوامر لمتاجر سلة وزد وشوبيفاي: أوصاف تبيع، وعناوين واضحة، وصفحات تجيب عن أسئلة العميل.",
            "Prompts for Salla, Zid and Shopify stores: descriptions that sell, clear titles, and pages that answer customer questions.")

P(s, "وصف منتج كامل", "Full Product Description",
  "عند إضافة منتج جديد إلى متجرك.",
  "When adding a new product to your store.",
  "أنت كاتب محتوى متخصص في التجارة الإلكترونية في السعودية. اكتب وصفًا لمنتج [اسم المنتج] لمتجري على [سلة / زد / شوبيفاي]. المعلومات: [المواصفات: المقاس، الخامة، اللون، الوزن...]. الجمهور: [وصف الجمهور]. التنسيق: فقرة افتتاحية من سطرين عن الفائدة، ثم 5 نقاط للمميزات، ثم قسم «محتويات العلبة»، ثم قسم «طريقة الاستخدام أو العناية». لا تضف أي مواصفات غير موجودة في المعلومات التي أعطيتك إياها.",
  "You are an e-commerce copywriter for the Saudi market. Write a description for [PRODUCT_NAME] for my [Salla / Zid / Shopify] store. Details: [SPECS: size, material, colour, weight...]. Audience: [AUDIENCE_DESCRIPTION]. Format: a two-line opening about the benefit, then 5 feature bullets, then a \"What's in the box\" section, then a \"How to use / care\" section. Do not add any specification that is not in the details I gave you.",
  "الجملة الأخيرة في الأمر («لا تضف مواصفات») مهمة جدًا؛ أدوات الذكاء الاصطناعي تميل لاختراع تفاصيل.",
  "The last sentence (\"do not add specs\") matters — AI tools tend to invent details otherwise.")

P(s, "عنوان منتج مناسب للبحث", "Search-Friendly Product Title",
  "عندما لا يظهر منتجك في نتائج البحث داخل المتجر أو في Google.",
  "When your product isn't showing up in store or Google search.",
  "اقترح 5 عناوين لمنتج [اسم المنتج] في متجر إلكتروني سعودي. كل عنوان لا يتجاوز 70 حرفًا، ويبدأ بالكلمة التي يبحث بها العميل غالبًا، ثم يضم أهم صفة (مثل [الصفة: المقاس، اللون، الماركة]). اكتب العناوين بالعربية، ثم اقترح لكل عنوان نسخة إنجليزية. وبعدها اقترح 10 كلمات بحث قد يكتبها العميل السعودي للوصول إلى هذا المنتج، بما فيها كلمات عامية شائعة.",
  "Suggest 5 titles for [PRODUCT_NAME] in a Saudi online store. Each title is under 70 characters, starts with the word customers most likely search for, then includes the key attribute (e.g. [ATTRIBUTE: size, colour, brand]). Write the titles in Arabic, then give an English version of each. Then suggest 10 search terms a Saudi customer might type to find this product, including common colloquial words.",
  "قارن الكلمات المقترحة بما يكتبه العملاء فعلًا في خانة البحث بمتجرك إن كانت المنصة توفر هذا التقرير.",
  "Compare the suggested keywords against what customers actually type in your store search, if your platform offers that report.")

P(s, "أسئلة شائعة لصفحة المنتج", "Product Page FAQ",
  "عندما تتكرر عليك نفس الأسئلة من العملاء.",
  "When customers keep asking you the same questions.",
  "اكتب قسم «الأسئلة الشائعة» لصفحة منتج [اسم المنتج]. هذه معلومات صحيحة عن المنتج والمتجر: [المعلومات: مدة التوصيل، سياسة الاسترجاع، طرق الدفع، الضمان]. اكتب 8 أسئلة يطرحها العميل السعودي عادة قبل الشراء، وأجب عنها بإيجاز ووضوح بناءً على المعلومات فقط. إذا كان سؤال مهم لا تتوفر له معلومات، اكتب بجانبه [يحتاج إجابة من صاحب المتجر] بدل أن تخترع إجابة.",
  "Write a FAQ section for the product page of [PRODUCT_NAME]. These are accurate facts about the product and store: [FACTS: delivery time, return policy, payment methods, warranty]. Write 8 questions Saudi customers usually ask before buying and answer them briefly, using only these facts. If an important question has no information, write [NEEDS ANSWER FROM STORE OWNER] instead of inventing one.",
  "ألصق رسائل العملاء الحقيقية (بعد حذف أسمائهم وأرقامهم) ليستخرج منها الأسئلة الأكثر تكرارًا.",
  "Paste real customer messages (with names and numbers removed) so it can pull out the most frequent questions.")

P(s, "وصف مختصر للجوال", "Short Mobile Description",
  "لأن أغلب عملائك يتصفحون من الجوال ولا يقرؤون النصوص الطويلة.",
  "Most shoppers browse on mobile and skip long text.",
  "لدي هذا الوصف الطويل لمنتج: [ألصق الوصف]. اختصره إلى نسخة للجوال لا تتجاوز 50 كلمة، تبدأ بأهم فائدة، وتتضمن 3 نقاط قصيرة جدًا بالرموز ✓، وتنتهي بسطر يشجع على الإضافة إلى السلة. لا تحذف أي معلومة مهمة عن المقاس أو الاستخدام.",
  "Here is a long product description: [PASTE_DESCRIPTION]. Shorten it into a mobile version of 50 words or fewer that opens with the main benefit, includes 3 very short ✓ bullets, and ends with a line encouraging add-to-cart. Do not remove any important sizing or usage information.",
  "ضع النسخة المختصرة في أعلى الصفحة، واترك الوصف الكامل تحتها لمن يريد التفاصيل.",
  "Put the short version at the top of the page and keep the full description below it for those who want detail.")

P(s, "وصف مجموعة أو تصنيف", "Collection / Category Description",
  "عند إنشاء تصنيف جديد في المتجر مثل «هدايا» أو «عطور».",
  "When creating a new store category, like \"Gifts\" or \"Perfumes\".",
  "اكتب نصًا تعريفيًا لصفحة تصنيف بعنوان [اسم التصنيف] في متجر [اسم المتجر]. المنتجات في التصنيف: [أمثلة على المنتجات]. اكتب فقرة من 60–80 كلمة تساعد العميل على الاختيار وتذكر لمن يناسب هذا التصنيف، ثم 3 عناوين فرعية قصيرة لتقسيم المنتجات (مثل حسب السعر أو المناسبة). اكتب أيضًا وصف ميتا (Meta Description) أقل من 155 حرفًا بالعربية وآخر بالإنجليزية.",
  "Write intro text for a category page called [CATEGORY_NAME] in [STORE_NAME]. Products in it: [EXAMPLE_PRODUCTS]. Write a 60–80 word paragraph that helps customers choose and says who the category suits, then 3 short sub-headings to group products (e.g. by price or occasion). Also write a meta description under 155 characters in Arabic and another in English.",
  "وصف الميتا هو ما يظهر تحت رابطك في نتائج Google؛ اجعله يجيب عن «لماذا أضغط هنا؟».",
  "The meta description is what appears under your link in Google results — make it answer \"why should I click?\"")

P(s, "مقارنة بين منتجين", "Two-Product Comparison",
  "عندما يتردد العميل بين منتجين في متجرك.",
  "When customers hesitate between two of your products.",
  "أعدّ جدول مقارنة واضحًا بين [المنتج الأول] و[المنتج الثاني] من متجري. المعلومات: [مواصفات وأسعار كل منتج]. الجدول يتضمن: السعر، أهم 4 مواصفات، ولمن يناسب كل منتج. بعد الجدول اكتب فقرة قصيرة بعنوان «أيهما تختار؟» تساعد العميل على القرار حسب احتياجه، بدون التقليل من أي منتج.",
  "Create a clear comparison table between [PRODUCT_1] and [PRODUCT_2] from my store. Details: [SPECS_AND_PRICES_OF_EACH]. The table includes: price, the 4 most important specs, and who each product suits. After the table, write a short paragraph titled \"Which one should you choose?\" that helps the customer decide based on their need, without putting either product down.",
  "يمكنك نشر نفس الجدول كصورة في القصص أو الرد به على العملاء في واتساب.",
  "You can also post the same table as an image in stories or send it to customers on WhatsApp.")

P(s, "صفحة سياسة الشحن والاسترجاع", "Shipping & Returns Policy Page",
  "عند إطلاق المتجر أو تحديث السياسات.",
  "When launching your store or updating policies.",
  "صغ صفحة «سياسة الشحن والاسترجاع» لمتجر [اسم المتجر] بلغة بسيطة وودودة. هذه هي القواعد التي قررتها: [مدة الشحن لكل مدينة، تكلفة الشحن، مدة الاسترجاع، شروط الاسترجاع، طريقة استرداد المبلغ]. نظّم الصفحة بعناوين فرعية وأسئلة وأجوبة قصيرة. لا تضف أي شرط لم أذكره. في النهاية أضف تنبيهًا لي (وليس للعميل) بالنقاط التي يُنصح بمراجعتها مع الأنظمة السعودية للتجارة الإلكترونية وحماية المستهلك.",
  "Draft a \"Shipping & Returns\" page for [STORE_NAME] in simple, friendly language. These are the rules I decided: [SHIPPING_TIME_PER_CITY, SHIPPING_COST, RETURN_WINDOW, RETURN_CONDITIONS, REFUND_METHOD]. Organise it with sub-headings and short Q&As. Do not add any condition I did not mention. At the end, add a note for me (not the customer) listing points I should check against Saudi e-commerce and consumer-protection regulations.",
  "هذا مسودة وليس استشارة قانونية؛ راجع نظام التجارة الإلكترونية ومتطلبات وزارة التجارة قبل النشر.",
  "This is a draft, not legal advice — check the Saudi E-Commerce Law and Ministry of Commerce requirements before publishing.")

# ---------------------------------------------------------------- 3
s = section("whatsapp", "ردود خدمة العملاء عبر واتساب", "WhatsApp Customer Service Replies",
            "ردود جاهزة ومهذبة لأكثر المواقف تكرارًا، يمكنك حفظها في «الردود السريعة» في واتساب للأعمال.",
            "Polite, ready replies for the most common situations — save them as Quick Replies in WhatsApp Business.")

P(s, "مكتبة ردود سريعة", "Quick Replies Library",
  "مرة واحدة عند إعداد واتساب للأعمال.",
  "Once, when setting up WhatsApp Business.",
  "أنت مسؤول خدمة عملاء في [نوع المشروع] اسمه [اسم المشروع] في السعودية. اكتب 12 ردًا سريعًا قصيرًا باللهجة السعودية المهذبة لهذه المواقف: الترحيب، أوقات العمل، الموقع، طرق الدفع، الأسعار، مدة التوصيل، تأكيد الطلب، شكر بعد الشراء، الاعتذار عن التأخير، طلب الانتظار، تحويل لموظف آخر، إنهاء المحادثة. اقترح لكل رد اختصارًا (مثل /ترحيب). استخدم هذه المعلومات: [أوقات العمل، الموقع، طرق الدفع، مدة التوصيل].",
  "You handle customer service for [BUSINESS_NAME], a [BUSINESS_TYPE] in Saudi Arabia. Write 12 short, polite quick replies in Saudi dialect for: greeting, working hours, location, payment methods, prices, delivery time, order confirmation, post-purchase thanks, apology for delay, please-wait, handover to a colleague, closing the chat. Suggest a shortcut for each (e.g. /welcome). Use this information: [WORKING_HOURS, LOCATION, PAYMENT_METHODS, DELIVERY_TIME].",
  "اجعل رسالة الترحيب تذكر أوقات الرد المتوقعة، فهذا يخفف الضغط عليك وعلى العميل.",
  "Make your greeting message mention expected reply times — it reduces pressure on you and the customer.",
  dialect=True)

P(s, "الرد على عميل غاضب", "Replying to an Angry Customer",
  "عندما تصلك رسالة شكوى حادة وتريد ردًا هادئًا ومحترفًا.",
  "When you receive a heated complaint and need a calm, professional reply.",
  "وصلتني هذه الرسالة من عميل غاضب: [ألصق رسالة العميل]. ما حدث فعلًا من جهتنا: [شرح مختصر للمشكلة]. ما يمكننا تقديمه: [الحل: استبدال، استرجاع، خصم، إعادة توصيل]. اكتب ردًا باللهجة السعودية المهذبة: يبدأ بتفهّم شعوره دون جدال، ثم اعتذار صادق إن كان الخطأ منا، ثم الحل بخطوات واضحة، ثم موعد محدد للمتابعة. لا تتجاوز 80 كلمة، ولا تقدّم وعودًا غير الحل المذكور.",
  "I received this message from an angry customer: [PASTE_CUSTOMER_MESSAGE]. What actually happened on our side: [SHORT_EXPLANATION]. What we can offer: [SOLUTION: replacement, refund, discount, re-delivery]. Write a reply in polite Saudi dialect: start by acknowledging their feelings without arguing, then a sincere apology if we were at fault, then the solution in clear steps, then a specific follow-up time. Keep it under 80 words and make no promises beyond the stated solution.",
  "لا ترد وأنت منفعل. ولّد الرد، انتظر دقيقتين، اقرأه مرة أخرى ثم أرسله.",
  "Don't reply while upset. Generate the reply, wait two minutes, re-read it, then send.",
  dialect=True)

P(s, "الرد على سؤال السعر (وش السعر؟)", "Answering \"How Much?\"",
  "عندما يسأل العميل عن السعر فقط دون تفاصيل.",
  "When a customer just asks the price without context.",
  "اكتب 3 ردود مختلفة باللهجة السعودية على عميل أرسل «بكم؟» أو «وش السعر؟» عن [المنتج أو الخدمة]. السعر: [السعر أو نطاق الأسعار]. كل رد يذكر السعر بوضوح، ثم يضيف ميزة واحدة تبرر القيمة، ثم يسأل سؤالًا واحدًا بسيطًا يساعد على إكمال البيع (مثل المقاس أو الموعد المناسب). لا تتجاوز 40 كلمة لكل رد.",
  "Write 3 different replies in Saudi dialect to a customer who just sent \"How much?\" about [PRODUCT_OR_SERVICE]. Price: [PRICE_OR_RANGE]. Each reply states the price clearly, adds one benefit that justifies the value, then asks one simple question that moves the sale forward (e.g. size or preferred time). Max 40 words each.",
  "اذكر السعر مباشرة؛ إخفاء السعر وطلب «تواصل خاص» يجعل كثيرًا من العملاء يغادرون.",
  "State the price directly — hiding it behind \"DM for price\" makes many customers leave.",
  dialect=True)

P(s, "متابعة سلة متروكة أو طلب لم يكتمل", "Following Up an Unfinished Order",
  "عندما يسأل العميل ثم يختفي، أو يترك منتجات في السلة.",
  "When a customer asks then goes quiet, or leaves items in the cart.",
  "اكتب رسالتي متابعة لطيفتين باللهجة السعودية لعميل سأل عن [المنتج] قبل [المدة] ولم يكمل الطلب. الرسالة الأولى تُرسل بعد يوم: تذكير ودّي وسؤال إن كان لديه أي استفسار. الرسالة الثانية تُرسل بعد 3 أيام: تذكير أخير مع [ميزة أو عرض إن وُجد]. كل رسالة أقل من 35 كلمة. يجب أن تكون النبرة خدومة وغير ملحّة، وأن تتضمن طريقة سهلة لإيقاف الرسائل.",
  "Write two gentle follow-up messages in Saudi dialect for a customer who asked about [PRODUCT] [TIME_AGO] and didn't complete the order. Message 1 (after one day): a friendly reminder asking if they have any questions. Message 2 (after 3 days): a final reminder with [BENEFIT_OR_OFFER_IF_ANY]. Each under 35 words. The tone should be helpful, not pushy, and include an easy way to opt out of further messages.",
  "توقف بعد رسالتين. الإلحاح الزائد يدفع العميل لحظر الرقم.",
  "Stop after two messages — over-following-up gets your number blocked.",
  dialect=True)

P(s, "تحديث حالة الطلب والتأخير", "Order Status & Delay Update",
  "عندما يتأخر الطلب أو تريد إبلاغ العميل بخطوات الشحن.",
  "When an order is delayed or you want to update the customer on shipping.",
  "اكتب 4 رسائل قصيرة لتحديث حالة الطلب لعملاء [اسم المتجر]: (1) تم استلام الطلب وجاري التجهيز، (2) تم الشحن مع رقم التتبع [رقم التتبع] ورابط [رابط التتبع]، (3) الطلب سيتأخر بسبب [سبب التأخير] والموعد الجديد [الموعد]، (4) تم التوصيل مع طلب لطيف للتقييم. اكتبها باللهجة السعودية، واجعل رسالة التأخير صادقة وتعتذر بوضوح دون إلقاء اللوم على العميل.",
  "Write 4 short order-status messages for customers of [STORE_NAME]: (1) order received and being prepared, (2) shipped, with tracking number [TRACKING_NUMBER] and link [TRACKING_LINK], (3) the order will be late because of [DELAY_REASON], new date [NEW_DATE], (4) delivered, with a gentle request for a review. Write them in Saudi dialect, and make the delay message honest with a clear apology, never blaming the customer.",
  "أبلغ العميل بالتأخير قبل أن يسألك هو؛ هذا وحده يقلل الشكاوى كثيرًا.",
  "Tell the customer about a delay before they ask — that alone prevents a lot of complaints.",
  dialect=True)

P(s, "الرد على طلب خصم", "Responding to a Discount Request",
  "عندما يطلب العميل «آخر سعر» أو خصمًا.",
  "When a customer asks for \"your best price\" or a discount.",
  "عميل يطلب خصمًا على [المنتج أو الخدمة] بسعر [السعر]. سياستي: [لا خصم / خصم محدود بنسبة كذا / هدية بدل الخصم / خصم للكميات]. اكتب ردين مهذبين باللهجة السعودية: الأول يرفض الخصم بلطف ويوضح القيمة، والثاني يقدّم البديل المسموح به حسب سياستي. حافظ على علاقة جيدة مع العميل ولا تجعله يشعر بالحرج.",
  "A customer is asking for a discount on [PRODUCT_OR_SERVICE] priced at [PRICE]. My policy: [no discount / limited discount of X% / free gift instead / bulk discount]. Write two polite replies in Saudi dialect: the first declines the discount kindly and explains the value; the second offers the alternative my policy allows. Keep the relationship warm and don't make the customer feel embarrassed.",
  "ثبّت سياسة الخصم مسبقًا واكتبها؛ التفاوض المختلف مع كل عميل يربك أسعارك.",
  "Set your discount policy in advance and write it down — negotiating differently with each customer muddles your pricing.",
  dialect=True)

P(s, "رسالة شكر وطلب تقييم", "Thank-You & Review Request",
  "بعد يوم أو يومين من استلام العميل لطلبه.",
  "One or two days after the customer receives their order.",
  "اكتب رسالة شكر قصيرة باللهجة السعودية لعميل اشترى [المنتج] من [اسم المشروع]. اسأله إن كان كل شيء على ما يرام، واطلب منه بلطف — دون أي ضغط ودون مقابل مشروط بتقييم إيجابي — أن يشاركنا رأيه عبر [رابط التقييم: Google أو المتجر]. أقل من 45 كلمة. اكتب نسخة ثانية رسمية أكثر للشركات.",
  "Write a short thank-you message in Saudi dialect for a customer who bought [PRODUCT] from [BUSINESS_NAME]. Ask if everything is fine and kindly invite them — with no pressure and no reward conditional on a positive review — to share their feedback via [REVIEW_LINK: Google or store]. Under 45 words. Write a second, more formal version for B2B clients.",
  "لا تقدّم هدية مقابل «تقييم 5 نجوم» فقط؛ هذا يخالف سياسات Google ويفقدك المصداقية.",
  "Never offer a gift in exchange for \"5-star reviews\" only — it breaks Google's policies and costs you credibility.",
  dialect=True)

# ---------------------------------------------------------------- 4
s = section("seasonal", "الحملات الموسمية", "Seasonal Campaigns",
            "رمضان، العيدين، اليوم الوطني، يوم التأسيس، الجمعة البيضاء، والعودة للمدارس. تأكد دائمًا من التواريخ الرسمية لكل سنة.",
            "Ramadan, both Eids, National Day, Founding Day, White Friday and Back to School. Always confirm each year's official dates.")

P(s, "تقويم المواسم السنوي", "Annual Seasons Calendar",
  "في بداية السنة لتخطيط حملاتك مسبقًا.",
  "At the start of the year to plan campaigns early.",
  "أعدّ تقويمًا تسويقيًا لعام [السنة] لمشروع [نوع المشروع] في السعودية يشمل: يوم التأسيس (22 فبراير)، شهر رمضان، عيد الفطر، عيد الأضحى، العودة للمدارس، اليوم الوطني السعودي (23 سبتمبر)، الجمعة البيضاء، ونهاية السنة. لكل مناسبة: متى أبدأ التحضير، متى أبدأ النشر، فكرة حملة مناسبة لمشروعي، ونوع العرض المقترح. للمناسبات الهجرية اكتب [التاريخ التقريبي — يُؤكَّد لاحقًا] بدل تحديد تاريخ ميلادي دقيق.",
  "Build a [YEAR] marketing calendar for a [BUSINESS_TYPE] in Saudi Arabia covering: Founding Day (22 February), Ramadan, Eid al-Fitr, Eid al-Adha, Back to School, Saudi National Day (23 September), White Friday, and year-end. For each occasion: when to start preparing, when to start posting, a campaign idea suited to my business, and a suggested offer type. For Hijri occasions, write [APPROXIMATE DATE — TO BE CONFIRMED] instead of a precise Gregorian date.",
  "المناسبات الهجرية تتقدم نحو 11 يومًا كل سنة ميلادية؛ تحقق من التقويم الرسمي (أم القرى) قبل التخطيط.",
  "Hijri occasions move about 11 days earlier each Gregorian year — check the official Umm al-Qura calendar before planning.")

P(s, "حملة رمضان", "Ramadan Campaign",
  "قبل رمضان بأربعة إلى ستة أسابيع.",
  "Four to six weeks before Ramadan.",
  "صمّم حملة رمضانية لمشروع [اسم المشروع] الذي يقدّم [المنتج أو الخدمة]. راعِ أن أوقات النشاط والتسوق تتغير في رمضان (بعد الإفطار وفي الليل). أريد: (1) فكرة الحملة واسمها، (2) 4 مراحل: قبل رمضان، العشر الأوائل، منتصف الشهر، العشر الأواخر واستعداد العيد، (3) 3 أفكار منشورات لكل مرحلة، (4) أفضل أوقات النشر المقترحة. النبرة روحانية ودافئة بعيدًا عن المبالغة التجارية، ودون استخدام الآيات القرآنية في الإعلانات.",
  "Design a Ramadan campaign for [BUSINESS_NAME], which offers [PRODUCT_OR_SERVICE]. Consider that activity and shopping times shift during Ramadan (after iftar and late at night). I want: (1) a campaign concept and name, (2) 4 phases: pre-Ramadan, first ten days, mid-month, last ten days and Eid preparation, (3) 3 post ideas per phase, (4) suggested best posting times. The tone should be warm and spiritual without heavy commercialism, and must not use Qur'anic verses in advertising.",
  "اختبر أوقات النشر بنفسك خلال الأسبوع الأول، ثم عدّل الخطة بناءً على تفاعل جمهورك الفعلي.",
  "Test posting times yourself during the first week, then adjust based on your audience's actual engagement.")

P(s, "تهنئة وعروض العيد", "Eid Greetings & Offers",
  "قبل عيد الفطر أو عيد الأضحى بأسبوعين.",
  "Two weeks before Eid al-Fitr or Eid al-Adha.",
  "اكتب لمشروع [اسم المشروع] بمناسبة [عيد الفطر / عيد الأضحى]: (1) 3 نصوص تهنئة قصيرة للمنشورات، واحدة رسمية وواحدة ودّية باللهجة السعودية وواحدة للعملاء من الشركات، (2) إعلانًا عن عرض العيد: [تفاصيل العرض ومدته]، (3) رسالة واتساب للعملاء المشتركين، (4) نصًا لإعلان أوقات العمل في العيد: [أوقات العمل]. استخدم عبارات تهنئة سعودية متداولة مثل «عساكم من عوّاده».",
  "For [BUSINESS_NAME], on the occasion of [Eid al-Fitr / Eid al-Adha], write: (1) 3 short greeting texts for posts — one formal, one friendly in Saudi dialect, one for business clients, (2) an announcement of the Eid offer: [OFFER_DETAILS_AND_DURATION], (3) a WhatsApp message for opted-in customers, (4) a notice of Eid working hours: [WORKING_HOURS]. Use common Saudi Eid greetings such as \"عساكم من عوّاده\".",
  "جهّز منشور أوقات العمل مبكرًا وثبّته في الحساب؛ هو أكثر ما يسأل عنه العملاء في العيد.",
  "Prepare the working-hours post early and pin it — it's what customers ask about most during Eid.",
  dialect=True)

P(s, "اليوم الوطني السعودي (23 سبتمبر)", "Saudi National Day (23 Sept)",
  "قبل اليوم الوطني بثلاثة أسابيع.",
  "Three weeks before National Day.",
  "أنشئ حملة لليوم الوطني السعودي (23 سبتمبر) لمشروع [اسم المشروع]. أريد: (1) 5 أفكار محتوى تعبّر عن الفخر والانتماء بطريقة مرتبطة بمجال [المجال]، (2) 3 نصوص قصيرة للمنشورات، (3) فكرة عرض مناسبة: [نوع العرض]، (4) ملاحظات حول الاستخدام الصحيح للهوية الوطنية. التزم بالذوق العام، ولا تقترح أي استخدام للعلم السعودي في منتجات أو أماكن لا تليق بمكانته (لأنه يحمل الشهادتين)، ولا تستخدم شعارات رسمية دون إذن.",
  "Create a Saudi National Day (23 September) campaign for [BUSINESS_NAME]. I want: (1) 5 content ideas expressing pride and belonging in a way linked to [INDUSTRY], (2) 3 short post texts, (3) a suitable offer idea: [OFFER_TYPE], (4) notes on correct use of national identity. Keep it respectful; do not suggest using the Saudi flag on products or in places unbefitting its status (it carries the Shahada), and do not use official logos without permission.",
  "إذا أعلنت هوية بصرية رسمية لليوم الوطني لهذا العام، فراجع دليل استخدامها المنشور من الجهة المعنية قبل التصميم.",
  "If an official National Day visual identity is released for the year, review its published usage guide before designing.")

P(s, "يوم التأسيس (22 فبراير)", "Founding Day (22 Feb)",
  "قبل يوم التأسيس بثلاثة أسابيع.",
  "Three weeks before Founding Day.",
  "اكتب حملة ليوم التأسيس السعودي (22 فبراير) لمشروع [اسم المشروع] في مجال [المجال]. يوم التأسيس يحتفي بجذور الدولة السعودية وتاريخها وتراثها. أريد: (1) 4 أفكار محتوى تربط مشروعي بالتراث السعودي (مثل الأزياء التقليدية، القهوة، العمارة النجدية، الحِرف)، (2) 3 نصوص منشورات، (3) فكرة عرض أو منتج خاص بالمناسبة. اكتب ملاحظة إن كان في المحتوى معلومة تاريخية يجب أن أتحقق منها من مصدر رسمي.",
  "Write a Saudi Founding Day (22 February) campaign for [BUSINESS_NAME] in [INDUSTRY]. Founding Day celebrates the roots, history and heritage of the Saudi state. I want: (1) 4 content ideas linking my business to Saudi heritage (e.g. traditional dress, coffee, Najdi architecture, crafts), (2) 3 post texts, (3) an offer or special product idea for the occasion. Flag any historical fact in the content that I should verify from an official source.",
  "لا تخلط بين يوم التأسيس واليوم الوطني؛ لكلٍّ منهما معنى مختلف، والعملاء يلاحظون ذلك.",
  "Don't confuse Founding Day with National Day — they mean different things, and customers notice.")

P(s, "الجمعة البيضاء", "White Friday",
  "قبل موسم الجمعة البيضاء (نوفمبر عادة) بشهر.",
  "A month before the White Friday season (usually November).",
  "خطط لعرض «الجمعة البيضاء» لمتجر [اسم المتجر]. المنتجات المشاركة: [المنتجات]، وهامش الربح التقريبي لكل منتج: [الهامش]. أريد: (1) 3 أنواع عروض مقترحة مع حساب بسيط يوضح أثر كل عرض على الربح، (2) جدولًا زمنيًا: قبل الأسبوع، يوم العرض، وبعده، (3) نصوص إعلان قصيرة، (4) قائمة تحقق للمخزون والشحن وخدمة العملاء. الأسعار قبل الخصم يجب أن تكون حقيقية، ولا تقترح رفع السعر ثم خصمه.",
  "Plan a White Friday offer for [STORE_NAME]. Participating products: [PRODUCTS], approximate margin per product: [MARGIN]. I want: (1) 3 offer types with a simple calculation of each offer's effect on profit, (2) a timeline: week before, offer day, after, (3) short ad copy, (4) a checklist for stock, shipping and customer service. Pre-discount prices must be genuine; do not suggest raising prices and then discounting them.",
  "تحقق من الحساب بنفسك؛ خصم 30% على منتج بهامش 35% يترك لك ربحًا ضئيلًا جدًا بعد الشحن.",
  "Check the maths yourself — a 30% discount on a product with a 35% margin leaves very little after shipping.")

P(s, "العودة للمدارس", "Back to School",
  "قبل بداية العام الدراسي بثلاثة أسابيع.",
  "Three weeks before the school year starts.",
  "اكتب حملة «العودة للمدارس» لمشروع [اسم المشروع] الذي يقدّم [المنتج أو الخدمة]. الجمهور الأساسي: أولياء الأمور في [المدينة]. أريد: (1) زاوية الحملة التي تخاطب احتياج الأهل (التنظيم، الوقت، الميزانية)، (2) 5 أفكار منشورات، (3) فكرة باقة أو حزمة منتجات، (4) رسالة واتساب قصيرة. تحقق من موعد بداية الدراسة في التقويم الدراسي الرسمي واكتب [موعد بدء الدراسة] كمتغير.",
  "Write a Back to School campaign for [BUSINESS_NAME], which offers [PRODUCT_OR_SERVICE]. Main audience: parents in [CITY]. I want: (1) a campaign angle addressing parents' needs (organisation, time, budget), (2) 5 post ideas, (3) a bundle idea, (4) a short WhatsApp message. Use [SCHOOL_START_DATE] as a variable — I'll confirm it from the official academic calendar.",
  "حتى لو لم يكن مشروعك تعليميًا، الأهالي يبحثون عن ما يوفّر وقتهم في هذا الموسم.",
  "Even if your business isn't education-related, parents look for anything that saves them time this season.")

P(s, "تهنئة ومحتوى لمناسبة خاصة", "Greeting for Any Occasion",
  "لأي مناسبة أخرى: افتتاح فرع، ذكرى تأسيس المشروع، موسم سياحي محلي.",
  "Any other occasion: branch opening, business anniversary, local tourism season.",
  "اكتب 3 منشورات لمشروع [اسم المشروع] بمناسبة [المناسبة] التي تصادف [التاريخ]. المنشور الأول: إعلان أو تهنئة. الثاني: قصة قصيرة عن المشروع أو الفريق مرتبطة بالمناسبة. الثالث: شكر للعملاء مع [العرض إن وُجد]. اكتب باللهجة السعودية الودّية. اجعل النص صادقًا ولا تذكر أرقام مبيعات أو عملاء غير موجودة في هذه المعلومات: [معلومات حقيقية عن المشروع].",
  "Write 3 posts for [BUSINESS_NAME] for [OCCASION] on [DATE]. Post 1: announcement or greeting. Post 2: a short story about the business or team tied to the occasion. Post 3: thanks to customers with [OFFER_IF_ANY]. Write in friendly Saudi dialect. Keep it genuine and do not mention sales or customer numbers that aren't in this information: [REAL_FACTS_ABOUT_THE_BUSINESS].",
  "القصص الحقيقية عن بدايتك وفريقك تتفاعل معها الناس أكثر من العروض.",
  "Real stories about how you started and your team often get more engagement than offers.",
  dialect=True)

# ---------------------------------------------------------------- 5
s = section("offers", "العروض وصفحات الأسعار", "Offers & Pricing Pages",
            "أوامر لصياغة الباقات وصفحات الأسعار وصفحات الهبوط بوضوح وصدق.",
            "Prompts to structure packages, pricing pages and landing pages clearly and honestly.")

P(s, "تصميم باقات الأسعار", "Designing Pricing Tiers",
  "عندما تريد تحويل خدمتك إلى باقات واضحة.",
  "When you want to turn your service into clear packages.",
  "أنا [المهنة: مصمم، مستشار، مدرب...] أقدم خدمة [الخدمة] في السعودية. تكلفتي التقريبية لكل عميل: [التكلفة]، والوقت الذي يستغرقه العمل: [الوقت]. اقترح 3 باقات (أساسية، متقدمة، شاملة) مع: اسم لكل باقة، ما تتضمنه، ما لا تتضمنه، ولمن تناسب. لا تحدد أسعارًا نهائية؛ بل اقترح طريقة حساب السعر لكل باقة بناءً على التكلفة والوقت، واترك السعر كـ [السعر].",
  "I'm a [PROFESSION: designer, consultant, coach...] offering [SERVICE] in Saudi Arabia. My approximate cost per client: [COST]; time the work takes: [TIME]. Propose 3 tiers (basic, advanced, complete) with: a name, what's included, what's not included, and who it suits. Don't set final prices; suggest a pricing method for each tier based on cost and time, and leave the price as [PRICE].",
  "الباقة الوسطى غالبًا هي التي تريد أن يختارها أغلب العملاء؛ اجعل قيمتها واضحة مقارنة بالأخريين.",
  "The middle tier is usually the one you want most clients to pick — make its value clear compared to the other two.")

P(s, "نص صفحة الأسعار", "Pricing Page Copy",
  "بعد تحديد الباقات، لكتابة صفحتها في موقعك أو متجرك.",
  "After defining tiers, to write the page on your site or store.",
  "اكتب نص صفحة أسعار لـ [اسم المشروع] بناءً على هذه الباقات: [ألصق تفاصيل الباقات والأسعار]. التنسيق: عنوان رئيسي، سطر فرعي، بطاقة لكل باقة (اسم، سعر، 4–6 نقاط، نص زر)، ثم قسم أسئلة شائعة من 5 أسئلة عن الدفع والإلغاء والتعديلات. اذكر بوضوح هل الأسعار شاملة ضريبة القيمة المضافة أم لا حسب ما يلي: [شاملة / غير شاملة]. لا تستخدم عبارات استعجال مصطنعة.",
  "Write pricing-page copy for [BUSINESS_NAME] based on these tiers: [PASTE_TIER_DETAILS_AND_PRICES]. Format: headline, sub-line, a card per tier (name, price, 4–6 bullets, button text), then a 5-question FAQ about payment, cancellation and revisions. State clearly whether prices include VAT, as follows: [INCLUSIVE / EXCLUSIVE]. Don't use artificial urgency phrases.",
  "ضريبة القيمة المضافة في السعودية 15%؛ تأكد من متطلبات العرض والفوترة من هيئة الزكاة والضريبة والجمارك إذا كنت مسجلًا.",
  "Saudi VAT is 15% — if you're registered, confirm display and invoicing requirements with ZATCA.")

P(s, "عرض سعر رسمي لعميل", "Formal Quotation for a Client",
  "عندما يطلب منك عميل (شركة غالبًا) عرض سعر مكتوبًا.",
  "When a client (often a company) asks for a written quote.",
  "اكتب عرض سعر رسميًا باللغة العربية الفصحى من [اسم المشروع] إلى [اسم العميل] لخدمة [الخدمة]. التفاصيل: [نطاق العمل، المخرجات، المدة، السعر، طريقة الدفع، صلاحية العرض]. التنسيق: مقدمة قصيرة، فهمنا لاحتياجكم، نطاق العمل بنقاط، الجدول الزمني، التكلفة وشروط الدفع، ما لا يشمله العرض، الخاتمة. أضف في النهاية نسخة إنجليزية مختصرة من نفس العرض.",
  "Write a formal quotation in Arabic from [BUSINESS_NAME] to [CLIENT_NAME] for [SERVICE]. Details: [SCOPE, DELIVERABLES, TIMELINE, PRICE, PAYMENT_TERMS, VALIDITY]. Format: short intro, our understanding of your needs, scope as bullets, timeline, cost and payment terms, exclusions, closing. Add a short English version of the same quote at the end.",
  "قسم «ما لا يشمله العرض» يحميك من طلبات إضافية مجانية لاحقًا.",
  "The \"exclusions\" section protects you from free extra requests later.")

P(s, "صفحة هبوط لعرض محدد", "Landing Page for a Single Offer",
  "عند إطلاق منتج أو خدمة أو دورة جديدة.",
  "When launching a new product, service or course.",
  "اكتب نص صفحة هبوط لعرض [اسم العرض] من [اسم المشروع]. الجمهور: [وصف الجمهور]. المشكلة التي يحلها: [المشكلة]. ما يحصل عليه العميل: [المحتويات]. السعر: [السعر]. الأقسام: عنوان رئيسي وسطر فرعي، المشكلة، الحل، ما ستحصل عليه، لمن هذا العرض ولمن لا يناسب، الأسئلة الشائعة، دعوة نهائية للإجراء. لا تكتب شهادات عملاء أو نتائج رقمية — اترك مكانًا بعنوان [آراء العملاء الحقيقية] إن وُجدت.",
  "Write landing-page copy for [OFFER_NAME] from [BUSINESS_NAME]. Audience: [AUDIENCE_DESCRIPTION]. Problem it solves: [PROBLEM]. What the customer gets: [CONTENTS]. Price: [PRICE]. Sections: headline and sub-line, the problem, the solution, what you get, who it's for and who it's not for, FAQ, final call to action. Don't write testimonials or numeric results — leave a placeholder titled [REAL CUSTOMER FEEDBACK] if any exists.",
  "قسم «لمن لا يناسب» يزيد الثقة ويقلل طلبات الاسترجاع.",
  "A \"who it's not for\" section builds trust and reduces refund requests.")

P(s, "عرض حزمة (Bundle)", "Bundle Offer",
  "عندما تريد رفع متوسط قيمة الطلب.",
  "When you want to raise average order value.",
  "لدي هذه المنتجات مع أسعارها وتكلفتها: [قائمة المنتجات: السعر / التكلفة]. اقترح 3 حزم منطقية يشتريها العميل معًا، ولكل حزمة: الاسم، المنتجات، سعر الحزمة المقترح، التوفير للعميل، وهامش الربح المتبقي لي. اعرض الحساب في جدول. ثم اكتب وصفًا تسويقيًا قصيرًا لكل حزمة.",
  "Here are my products with prices and costs: [PRODUCT_LIST: price / cost]. Suggest 3 logical bundles customers would buy together. For each: name, products, suggested bundle price, customer saving, and my remaining margin. Show the maths in a table. Then write a short marketing description for each bundle.",
  "راجع كل رقم في الجدول بآلة حاسبة؛ النماذج اللغوية قد تخطئ في العمليات الحسابية.",
  "Double-check every number with a calculator — language models can make arithmetic mistakes.")

P(s, "شرح سبب السعر", "Explaining Your Price",
  "عندما يقارنك العملاء بمنافس أرخص.",
  "When customers compare you to a cheaper competitor.",
  "عملاء كثيرون يقولون إن سعر [المنتج أو الخدمة] لدينا ([السعر]) أعلى من غيرنا. هذه أسباب حقيقية لفرق السعر: [الأسباب: خامات، ضمان، خبرة، خدمة ما بعد البيع]. اكتب: (1) فقرة قصيرة لصفحة المنتج تشرح القيمة دون مهاجمة المنافسين، (2) رد واتساب من 3 أسطر باللهجة السعودية، (3) منشور تعليمي يشرح للعملاء ما يجب أن ينتبهوا له عند الشراء في هذا المجال.",
  "Many customers say our price for [PRODUCT_OR_SERVICE] ([PRICE]) is higher than others. These are the real reasons for the difference: [REASONS: materials, warranty, expertise, after-sales service]. Write: (1) a short product-page paragraph explaining the value without attacking competitors, (2) a 3-line WhatsApp reply in Saudi dialect, (3) an educational post explaining what customers should look for when buying in this field.",
  "المنشور التعليمي يقنع أكثر من الدفاع المباشر عن السعر.",
  "The educational post persuades better than directly defending your price.",
  dialect=True)

# ---------------------------------------------------------------- 6
s = section("reviews", "خرائط Google والرد على التقييمات", "Google Maps & Review Replies",
            "حسّن ملف نشاطك التجاري على خرائط Google ورد على التقييمات باحترافية.",
            "Improve your Google Business Profile and reply to reviews professionally.")

P(s, "وصف النشاط في ملف Google", "Google Business Profile Description",
  "عند إنشاء أو تحديث ملف نشاطك على Google.",
  "When creating or updating your Google Business Profile.",
  "اكتب وصفًا لملف النشاط التجاري على Google لـ [اسم المشروع]، وهو [نوع المشروع] في حي [الحي] بمدينة [المدينة]. الخدمات: [الخدمات]. ما يميزنا: [المميزات الحقيقية]. الوصف لا يتجاوز 750 حرفًا، يبدأ بما يقدمه المشروع بوضوح، ويتضمن اسم المدينة والحي بشكل طبيعي. اكتب نسخة عربية وأخرى إنجليزية. لا تضع روابط أو أرقام هواتف أو عروضًا داخل الوصف.",
  "Write a Google Business Profile description for [BUSINESS_NAME], a [BUSINESS_TYPE] in [DISTRICT], [CITY]. Services: [SERVICES]. What sets us apart: [REAL_DIFFERENTIATORS]. Max 750 characters, open with a clear statement of what the business offers, and naturally include the city and district. Write an Arabic and an English version. No links, phone numbers or promotions in the description.",
  "أضف صورًا حقيقية حديثة للمكان والمنتجات وحدّث أوقات العمل في المواسم؛ هذا أهم من الوصف نفسه.",
  "Add recent real photos of the place and products, and update hours during holidays — this matters more than the description itself.")

P(s, "الرد على تقييم إيجابي", "Replying to a Positive Review",
  "عند وصول تقييم جيد.",
  "When you get a good review.",
  "اكتب 3 ردود مختلفة على هذا التقييم الإيجابي في خرائط Google: [ألصق التقييم]. الردود قصيرة (2–3 أسطر)، شخصية، تذكر شيئًا محددًا ذكره العميل، وتتضمن دعوة لطيفة للعودة. لغة الرد: نفس لغة التقييم (عربية أو إنجليزية). وقّع باسم [اسم الموقّع] من فريق [اسم المشروع].",
  "Write 3 different replies to this positive Google Maps review: [PASTE_REVIEW]. Replies are short (2–3 lines), personal, mention something specific the customer said, and include a warm invitation to return. Reply language: same as the review (Arabic or English). Sign as [SIGNER_NAME] from the [BUSINESS_NAME] team.",
  "لا تنسخ نفس الرد لكل التقييمات؛ القراء يلاحظون الردود المكررة.",
  "Don't paste the same reply under every review — readers notice copy-paste responses.")

P(s, "الرد على تقييم سلبي", "Replying to a Negative Review",
  "عند وصول تقييم سلبي، حتى لو شعرت أنه غير منصف.",
  "When you get a negative review, even if you feel it's unfair.",
  "وصلنا هذا التقييم السلبي على خرائط Google: [ألصق التقييم]. ما حدث من وجهة نظرنا: [شرح مختصر]. اكتب ردًا علنيًا محترفًا: يشكر العميل على ملاحظته، يعتذر عن تجربته دون الاعتراف بأمور غير صحيحة، يوضح بإيجاز ما تم أو سيتم تحسينه، ويدعوه للتواصل على [وسيلة التواصل] لحل الأمر. لا تجادل، ولا تكشف أي معلومات شخصية عن العميل، ولا تتجاوز 70 كلمة.",
  "We received this negative Google Maps review: [PASTE_REVIEW]. What happened from our side: [SHORT_EXPLANATION]. Write a professional public reply that thanks the customer for the feedback, apologises for their experience without admitting things that aren't true, briefly says what was or will be improved, and invites them to contact [CONTACT_METHOD] to resolve it. Don't argue, don't reveal any personal customer information, and keep it under 70 words.",
  "الرد موجّه للعملاء المحتملين الذين يقرؤون أكثر من صاحب التقييم نفسه؛ اكتب له وأنت تتخيلهم.",
  "Your reply is really for future customers reading it, more than the reviewer — write with them in mind.")

P(s, "الرد على تقييم بدون نص", "Replying to Star-Only Reviews",
  "عند وصول تقييمات بالنجوم فقط دون تعليق.",
  "For reviews with stars but no comment.",
  "اكتب 10 ردود قصيرة جدًا ومتنوعة (سطر واحد) على تقييمات بالنجوم بدون تعليق لـ [اسم المشروع]: 5 ردود لتقييمات 4–5 نجوم (شكر ودعوة للعودة)، و5 ردود لتقييمات 1–3 نجوم (شكر واعتذار ودعوة لمشاركة التفاصيل عبر [وسيلة التواصل]). اجعل نصفها بالعربية ونصفها بالإنجليزية.",
  "Write 10 very short, varied (one-line) replies to star-only reviews for [BUSINESS_NAME]: 5 for 4–5 star ratings (thanks and invite back), and 5 for 1–3 star ratings (thanks, apology, invitation to share details via [CONTACT_METHOD]). Make half in Arabic and half in English.",
  "خصص وقتًا أسبوعيًا ثابتًا للرد على كل التقييمات الجديدة.",
  "Set a fixed weekly time to reply to all new reviews.")

P(s, "تحليل التقييمات لتحسين العمل", "Analysing Reviews for Improvements",
  "كل شهر أو ربع سنة.",
  "Monthly or quarterly.",
  "هذه مجموعة من تقييمات عملائنا (بعد حذف الأسماء): [ألصق التقييمات]. حلّلها واستخرج: (1) أكثر 3 أشياء يمدحها العملاء، (2) أكثر 3 شكاوى متكررة، (3) اقتراحات تحسين عملية لكل شكوى مرتبة حسب سهولة التنفيذ، (4) عبارات إيجابية استخدمها العملاء يمكنني الاستفادة من فكرتها في التسويق. اعتمد فقط على النص المرفق ولا تفترض أشياء غير مذكورة.",
  "Here is a set of our customer reviews (names removed): [PASTE_REVIEWS]. Analyse them and extract: (1) the top 3 things customers praise, (2) the top 3 recurring complaints, (3) practical improvements for each complaint, ordered by ease of implementation, (4) positive phrases customers used whose ideas I could draw on in marketing. Rely only on the attached text and don't assume anything not mentioned.",
  "إذا أردت اقتباس تقييم عميل في إعلان، اقتبسه حرفيًا واستأذنه إن أمكن، ولا تعدّل كلامه.",
  "If you quote a customer review in an ad, quote it word for word, ask permission where possible, and never edit their words.")

P(s, "بطاقة دعوة للتقييم", "Review Request Card",
  "لطباعتها ووضعها على الكاشير أو داخل الطلبات.",
  "To print for the counter or include in orders.",
  "اكتب نصًا لبطاقة صغيرة (بحجم بطاقة العمل) تُوضع مع الطلبات أو على الكاشير في [اسم المشروع]، تدعو العميل لتقييمنا على خرائط Google عبر رمز QR. النص: عنوان من 4 كلمات، سطر واحد يشرح لماذا يهمنا رأيه، وتعليمات من خطوتين. اكتب 3 خيارات بالعربية وخيارًا بالإنجليزية. لا تَعِد بأي مكافأة مقابل التقييم.",
  "Write text for a small card (business-card size) to include with orders or place at the counter of [BUSINESS_NAME], inviting customers to review us on Google Maps via a QR code. Text: a 4-word heading, one line on why their opinion matters, and two-step instructions. Write 3 Arabic options and one English option. Don't promise any reward for reviewing.",
  "يمكنك إنشاء رابط التقييم المباشر من لوحة ملف نشاطك على Google ثم تحويله إلى رمز QR.",
  "You can get a direct review link from your Google Business Profile dashboard and turn it into a QR code.")

# ---------------------------------------------------------------- 7
s = section("hr", "التوظيف والموارد البشرية", "Hiring & HR",
            "إعلانات وظائف، أسئلة مقابلات، وتجهيز الموظف الجديد. راجع دائمًا نظام العمل السعودي ومنصة قوى في الأمور النظامية.",
            "Job ads, interview questions and onboarding. Always check the Saudi Labor Law and the Qiwa platform for regulatory matters.")

P(s, "إعلان وظيفة", "Job Advertisement",
  "عند فتح وظيفة جديدة.",
  "When opening a new position.",
  "اكتب إعلان وظيفة لمنصب [المسمى الوظيفي] في [اسم المشروع] بمدينة [المدينة]. نوع الدوام: [كامل / جزئي / عن بعد / مرن]. المهام الأساسية: [المهام]. المتطلبات: [المتطلبات]. ما نقدمه: [الراتب أو النطاق، المزايا]. التنسيق: مقدمة قصيرة عن المشروع، المهام، المتطلبات، ما نقدمه، طريقة التقديم عبر [طريقة التقديم]. اجعل الإعلان واضحًا ومحترمًا، وتجنب أي شروط تمييزية غير مرتبطة بالعمل. اكتب نسخة عربية وأخرى إنجليزية.",
  "Write a job ad for a [JOB_TITLE] at [BUSINESS_NAME] in [CITY]. Type: [full-time / part-time / remote / flexible]. Key duties: [DUTIES]. Requirements: [REQUIREMENTS]. What we offer: [SALARY_OR_RANGE, BENEFITS]. Format: short intro to the business, duties, requirements, what we offer, how to apply via [APPLICATION_METHOD]. Keep it clear and respectful, avoiding any discriminatory conditions unrelated to the job. Write an Arabic and an English version.",
  "ذكر نطاق الراتب يوفر وقتك ووقت المتقدمين، ويجذب المرشحين الجادين.",
  "Stating a salary range saves you and applicants time and attracts serious candidates.")

P(s, "أسئلة مقابلة عمل", "Interview Questions",
  "قبل مقابلة مرشح.",
  "Before interviewing a candidate.",
  "أعدّ 12 سؤال مقابلة لوظيفة [المسمى الوظيفي] في [نوع المشروع]. قسّمها: 4 أسئلة عن الخبرة والمهارات، 4 أسئلة سلوكية («حدثني عن موقف...»)، 2 سؤال لموقف عملي من واقع عملنا مثل [موقف حقيقي من العمل]، و2 سؤال عن التوقعات والالتزام. لكل سؤال: ما الذي أبحث عنه في الإجابة الجيدة. تجنب الأسئلة الشخصية غير المرتبطة بالعمل.",
  "Prepare 12 interview questions for a [JOB_TITLE] at a [BUSINESS_TYPE]. Split them: 4 on experience and skills, 4 behavioural (\"Tell me about a time...\"), 2 practical scenarios from our real work such as [REAL_WORK_SITUATION], and 2 about expectations and commitment. For each, note what a good answer looks like. Avoid personal questions unrelated to the job.",
  "اسأل كل المرشحين نفس الأسئلة ودوّن ملاحظاتك فورًا؛ هذا يجعل المقارنة عادلة.",
  "Ask every candidate the same questions and write notes immediately — it makes comparison fair.")

P(s, "نموذج تقييم المرشحين", "Candidate Scoring Sheet",
  "عند وجود أكثر من مرشح للوظيفة.",
  "When you have several candidates for a role.",
  "أنشئ نموذج تقييم للمرشحين لوظيفة [المسمى الوظيفي] على شكل جدول. المعايير: [المعايير: مهارة تقنية، تواصل، خبرة، التزام...]. لكل معيار: وزن نسبي، ووصف لما يعنيه التقييم 1 و3 و5. أضف عمودًا للملاحظات وصفًا لحساب الدرجة النهائية. اجعله بسيطًا بحيث أستطيع نسخه إلى Excel أو Google Sheets.",
  "Create a candidate scoring sheet for a [JOB_TITLE] as a table. Criteria: [CRITERIA: technical skill, communication, experience, commitment...]. For each criterion: a relative weight, and a description of what scores 1, 3 and 5 mean. Add a notes column and a row explaining how to calculate the final score. Keep it simple enough to copy into Excel or Google Sheets.",
  "حدد المعايير وأوزانها قبل المقابلات، وليس بعدها.",
  "Set the criteria and weights before the interviews, not after.")

P(s, "خطة أول أسبوع للموظف الجديد", "New Hire First-Week Plan",
  "قبل انضمام موظف جديد.",
  "Before a new employee starts.",
  "أعدّ خطة استقبال وتهيئة لأول 5 أيام لموظف جديد بوظيفة [المسمى الوظيفي] في [اسم المشروع]. لكل يوم: الأهداف، المهام، من يرافقه، وما يجب أن يتعلمه. أضف قائمة تحقق بالأمور الإدارية التي يجب تجهيزها قبل وصوله (حسابات، أدوات، عقد، تعريف بالفريق)، ورسالة ترحيب قصيرة تُرسل له قبل يوم من بدء العمل.",
  "Create a 5-day onboarding plan for a new [JOB_TITLE] at [BUSINESS_NAME]. For each day: goals, tasks, who accompanies them, and what they should learn. Add a checklist of admin items to prepare before they arrive (accounts, tools, contract, team introduction), and a short welcome message to send them the day before they start.",
  "تأكد من توثيق العقد عبر منصة قوى حسب المتطلبات النظامية المعمول بها.",
  "Make sure the contract is documented through the Qiwa platform as required by current regulations.")

P(s, "وصف وظيفي ومسؤوليات", "Job Description & Responsibilities",
  "عندما تريد توضيح مسؤوليات موظف حالي أو جديد.",
  "When you need to clarify responsibilities for a current or new employee.",
  "اكتب وصفًا وظيفيًا رسميًا لوظيفة [المسمى الوظيفي] في [اسم المشروع]. يشمل: الغرض من الوظيفة، المرجع الوظيفي (لمن يتبع)، المسؤوليات الأساسية (8–10 نقاط)، مؤشرات قياس الأداء المقترحة (4–5 مؤشرات قابلة للقياس)، المهارات المطلوبة، وساعات العمل [ساعات العمل]. اكتب بالعربية الفصحى، وأضف ملاحظة لي عن النقاط التي يجب أن تتوافق مع عقد العمل ونظام العمل.",
  "Write a formal job description for a [JOB_TITLE] at [BUSINESS_NAME]. Include: purpose of the role, reporting line, core responsibilities (8–10 bullets), suggested KPIs (4–5 measurable ones), required skills, and working hours [WORKING_HOURS]. Write in Modern Standard Arabic and add a note to me on points that must align with the employment contract and the Labor Law.",
  "شارك الوصف مع الموظف واتفقا عليه؛ الوضوح يقلل الخلافات لاحقًا.",
  "Share the description with the employee and agree on it together — clarity prevents disputes later.")

P(s, "رسالة اعتذار لمرشح", "Candidate Rejection Message",
  "بعد انتهاء المقابلات واختيار مرشح آخر.",
  "After interviews, once you've chosen someone else.",
  "اكتب رسالة اعتذار مهذبة لمرشح تمت مقابلته لوظيفة [المسمى الوظيفي] ولم يتم اختياره. الرسالة تشكره على وقته، تبلغه بالقرار بوضوح ولطف، و[اختياري: تذكر نقطة إيجابية لاحظناها: النقطة]، وتخبره أننا سنحتفظ بملفه للفرص القادمة إن وافق. اكتب نسخة بالعربية وأخرى بالإنجليزية، كل منها أقل من 90 كلمة.",
  "Write a polite rejection message to a candidate interviewed for [JOB_TITLE] who wasn't selected. It thanks them for their time, delivers the decision clearly and kindly, [optional: mentions a positive point we noticed: POINT], and says we'll keep their profile for future roles if they agree. Write Arabic and English versions, each under 90 words.",
  "الرد على كل المرشحين — حتى بالرفض — يبني سمعة جيدة لمشروعك في سوق صغير.",
  "Replying to every candidate — even with a no — builds your reputation in a small market.")

# ---------------------------------------------------------------- 8
s = section("finance", "التخطيط والأساسيات المالية", "Planning & Finance Basics",
            "أوامر تساعدك على التفكير وتنظيم الأرقام. الذكاء الاصطناعي ليس محاسبًا قانونيًا؛ راجع الأرقام والقرارات المهمة مع مختص.",
            "Prompts to help you think and organise numbers. AI is not a certified accountant — review important figures and decisions with a professional.")

P(s, "مخطط خطة عمل", "Business Plan Outline",
  "عند بدء مشروع جديد أو التقديم على تمويل.",
  "When starting a business or applying for funding.",
  "ساعدني في إعداد مخطط خطة عمل لمشروع [وصف المشروع] في [المدينة]. أريد هيكلًا بالعناوين التالية: الملخص التنفيذي، المشكلة والحل، السوق المستهدف، المنافسون، نموذج الإيرادات، خطة التسويق، الفريق، الخطة التشغيلية، التوقعات المالية، المخاطر. تحت كل عنوان اكتب الأسئلة التي يجب أن أجيب عنها، ولا تكتب الإجابات نيابة عني ولا تخترع أرقامًا عن حجم السوق.",
  "Help me outline a business plan for [BUSINESS_DESCRIPTION] in [CITY]. I want a structure with these headings: executive summary, problem and solution, target market, competitors, revenue model, marketing plan, team, operations plan, financial projections, risks. Under each heading list the questions I must answer — don't write the answers for me and don't invent market-size numbers.",
  "بعد أن تكتب إجاباتك، ألصقها واطلب منه أن «يكتشف الثغرات والافتراضات الضعيفة».",
  "Once you've written your answers, paste them back and ask it to \"find gaps and weak assumptions\".")

P(s, "جدول تدفق نقدي بسيط", "Simple Cash-Flow Table",
  "كل شهر لمعرفة هل ستكفي السيولة.",
  "Monthly, to check whether cash will last.",
  "أنشئ جدول تدفق نقدي لمدة [عدد الأشهر] أشهر لمشروعي. الرصيد الحالي: [الرصيد] ريال. الإيرادات المتوقعة شهريًا: [الإيرادات]. المصاريف الثابتة: [الإيجار، الرواتب، الاشتراكات...]. المصاريف المتغيرة: [المشتريات، الشحن، الإعلانات...]. الأعمدة: الشهر، الرصيد الافتتاحي، الإيرادات، المصاريف، صافي التدفق، الرصيد الختامي. أعطني أيضًا المعادلات لنقله إلى Google Sheets، ونبّهني إلى الشهر الذي قد يصبح فيه الرصيد منخفضًا.",
  "Build a [NUMBER_OF_MONTHS]-month cash-flow table for my business. Current balance: [BALANCE] SAR. Expected monthly revenue: [REVENUE]. Fixed costs: [RENT, SALARIES, SUBSCRIPTIONS...]. Variable costs: [PURCHASES, SHIPPING, ADS...]. Columns: month, opening balance, revenue, expenses, net flow, closing balance. Also give me the formulas to move it into Google Sheets, and flag any month where the balance may run low.",
  "استخدم الجدول الذي ينتجه كقالب فقط، وأدخل الأرقام الفعلية في Google Sheets حيث تكون المعادلات دقيقة.",
  "Use the generated table as a template only — enter real figures in Google Sheets, where formulas compute reliably.")

P(s, "حساب نقطة التعادل", "Break-Even Calculation",
  "قبل تحديد سعر منتج أو فتح فرع جديد.",
  "Before pricing a product or opening a new branch.",
  "اشرح لي خطوة بخطوة كيف أحسب نقطة التعادل لمشروعي، ثم احسبها بهذه الأرقام: المصاريف الثابتة الشهرية [المبلغ] ريال، سعر بيع الوحدة [السعر] ريال، التكلفة المتغيرة للوحدة [التكلفة] ريال. أظهر المعادلة وكل خطوة حسابية. ثم أعطني 3 سيناريوهات: لو رفعت السعر 10%، لو خفضت التكلفة 10%، لو زادت المصاريف الثابتة 20%.",
  "Explain step by step how to calculate my break-even point, then calculate it with these figures: monthly fixed costs [AMOUNT] SAR, unit selling price [PRICE] SAR, variable cost per unit [COST] SAR. Show the formula and every calculation step. Then give me 3 scenarios: price +10%, cost −10%, fixed costs +20%.",
  "اطلب منه إظهار خطوات الحساب دائمًا؛ هذا يسهّل عليك اكتشاف أي خطأ.",
  "Always ask it to show the calculation steps — it makes mistakes easy to spot.")

P(s, "تصنيف المصاريف", "Categorising Expenses",
  "نهاية كل شهر.",
  "At the end of each month.",
  "هذه قائمة مصاريفي لهذا الشهر: [ألصق القائمة: الوصف والمبلغ]. صنّفها في فئات (إيجار، رواتب، مشتريات، تسويق، اشتراكات تقنية، نقل وشحن، رسوم حكومية، أخرى). أعطني جدولًا بالإجمالي لكل فئة ونسبتها من المجموع، ثم 3 ملاحظات عن أين يمكن التوفير. لا تفترض أي مصروف غير موجود في القائمة.",
  "Here is my expense list for this month: [PASTE_LIST: description and amount]. Group them into categories (rent, salaries, purchases, marketing, tech subscriptions, transport & shipping, government fees, other). Give me a table with the total per category and its share of the whole, then 3 notes on where I could save. Don't assume any expense that isn't on the list.",
  "لا تلصق أرقام حسابات بنكية أو بطاقات أو هويات في أي أداة ذكاء اصطناعي.",
  "Never paste bank account numbers, card numbers or ID numbers into any AI tool.")

P(s, "تحليل SWOT", "SWOT Analysis",
  "عند التخطيط للسنة أو اتخاذ قرار كبير.",
  "When planning the year or making a big decision.",
  "أجرِ تحليل SWOT (نقاط القوة، الضعف، الفرص، التهديدات) لمشروع [وصف المشروع] في [المدينة]. هذه معلومات عن وضعنا الحالي: [المعلومات: الفريق، المنتجات، العملاء، المنافسون، التحديات]. لكل قسم 4–5 نقاط مبنية على المعلومات فقط. ثم اقترح 3 إجراءات عملية للأشهر الثلاثة القادمة تستفيد من نقاط القوة والفرص.",
  "Run a SWOT analysis (strengths, weaknesses, opportunities, threats) for [BUSINESS_DESCRIPTION] in [CITY]. Here's our current situation: [INFO: team, products, customers, competitors, challenges]. 4–5 points per quadrant based only on this information. Then suggest 3 practical actions for the next three months that build on strengths and opportunities.",
  "كلما كانت المعلومات التي تعطيها أدق وأصدق، كان التحليل أنفع.",
  "The more accurate and honest the information you give, the more useful the analysis.")

P(s, "أهداف ربع سنوية", "Quarterly Goals",
  "في بداية كل ربع سنة.",
  "At the start of each quarter.",
  "ساعدني في تحديد 3 أهداف لمشروعي للربع القادم بطريقة SMART (محددة، قابلة للقياس، قابلة للتحقيق، ذات صلة، محددة بوقت). وضعنا الحالي: [الوضع الحالي]. ما أريد تحقيقه بشكل عام: [الطموح]. لكل هدف: المؤشر الذي سأقيسه، الرقم المستهدف [اتركه لي لأحدده]، و4 مهام أسبوعية تقرّبني منه. ثم اكتب جدول متابعة أسبوعيًا بسيطًا.",
  "Help me set 3 SMART goals (specific, measurable, achievable, relevant, time-bound) for my business next quarter. Current situation: [CURRENT_SITUATION]. What I broadly want to achieve: [AMBITION]. For each goal: the metric I'll track, the target number [LEAVE FOR ME TO SET], and 4 weekly tasks that move me toward it. Then write a simple weekly tracking table.",
  "ثلاثة أهداف تكفي. أكثر من ذلك يشتت التركيز في مشروع صغير.",
  "Three goals is enough — more scatters focus in a small business.")

# ---------------------------------------------------------------- 9
s = section("productivity", "الإنتاجية والبريد والاجتماعات", "Productivity, Email & Meetings",
            "وفّر وقتك في الكتابة اليومية: رسائل بريد، ملخصات اجتماعات، وتنظيم المهام.",
            "Save time on daily writing: emails, meeting summaries and task organisation.")

P(s, "كتابة بريد إلكتروني رسمي", "Writing a Formal Email",
  "عند مراسلة جهة حكومية أو شركة أو مورد.",
  "When writing to a government entity, company or supplier.",
  "اكتب بريدًا إلكترونيًا رسميًا باللغة العربية الفصحى من [اسمي ومنصبي] في [اسم المشروع] إلى [الجهة أو الشخص]. الغرض: [الغرض]. النقاط التي يجب ذكرها: [النقاط]. التنسيق: عنوان موضوع واضح، تحية رسمية مناسبة، فقرة الغرض، النقاط، الطلب المحدد مع موعد إن وجد، الختام والتوقيع. اكتب أيضًا نسخة إنجليزية من نفس البريد.",
  "Write a formal email in Modern Standard Arabic from [MY_NAME_AND_TITLE] at [BUSINESS_NAME] to [ENTITY_OR_PERSON]. Purpose: [PURPOSE]. Points to include: [POINTS]. Format: clear subject line, appropriate formal greeting, purpose paragraph, the points, a specific request with a deadline if any, closing and signature. Also write an English version of the same email.",
  "اقرأ البريد بصوت عالٍ قبل إرساله؛ إن بدا متكلفًا اطلب «اجعله أبسط وأكثر مباشرة».",
  "Read it aloud before sending — if it sounds stiff, ask \"make it simpler and more direct\".")

P(s, "ملخص اجتماع ومهام", "Meeting Summary & Action Items",
  "بعد أي اجتماع مع الفريق أو العميل.",
  "After any team or client meeting.",
  "هذه ملاحظاتي (أو نص التفريغ) من اجتماع [موضوع الاجتماع] بتاريخ [التاريخ]: [ألصق الملاحظات]. لخّصها في: (1) ملخص من 3 أسطر، (2) القرارات التي اتُّخذت، (3) جدول مهام: المهمة، المسؤول، الموعد النهائي، (4) أسئلة ما زالت مفتوحة. إذا لم يُذكر مسؤول أو موعد لمهمة، اكتب [غير محدد] ولا تفترضه. ثم اكتب رسالة متابعة قصيرة أرسلها للحضور.",
  "Here are my notes (or transcript) from the [MEETING_TOPIC] meeting on [DATE]: [PASTE_NOTES]. Summarise into: (1) a 3-line summary, (2) decisions made, (3) an action table: task, owner, deadline, (4) open questions. If an owner or deadline wasn't mentioned, write [NOT SPECIFIED] rather than guessing. Then write a short follow-up message to send to attendees.",
  "احصل على موافقة الحضور قبل تسجيل الاجتماع، واحذف المعلومات الحساسة قبل لصق النص.",
  "Get attendees' consent before recording, and remove sensitive information before pasting a transcript.")

P(s, "الرد على بريد طويل", "Replying to a Long Email",
  "عندما يصلك بريد طويل ولا تعرف من أين تبدأ.",
  "When you get a long email and don't know where to start.",
  "وصلني هذا البريد: [ألصق البريد]. أولًا: لخّص لي ما يطلبه المرسل في 3 نقاط وأي مواعيد مذكورة. ثانيًا: اكتب ردًا [رسميًا / ودّيًا] يتضمن موقفي التالي: [موقفي أو قراري]. الرد واضح ومختصر ويجيب عن كل نقطة طلبها المرسل. اكتب الرد بنفس لغة البريد الأصلي.",
  "I received this email: [PASTE_EMAIL]. First: summarise what the sender is asking in 3 points, plus any deadlines mentioned. Second: write a [formal / friendly] reply that includes my position: [MY_POSITION_OR_DECISION]. The reply is clear, concise, and answers every point the sender raised. Write it in the same language as the original email.",
  "تحقق أن الرد لم يُضِف التزامات أو مواعيد لم تقررها أنت.",
  "Check the reply hasn't added commitments or deadlines you didn't decide on.")

P(s, "ترتيب الأولويات اليومية", "Daily Priorities",
  "صباح كل يوم مزدحم.",
  "On the morning of any busy day.",
  "هذه قائمة مهامي اليوم: [ألصق القائمة]. لدي [عدد الساعات] ساعات عمل متاحة، والتزامات ثابتة في [الأوقات]. رتّب المهام باستخدام مصفوفة أيزنهاور (عاجل/مهم)، ثم اقترح جدولًا زمنيًا لليوم يضع المهام التي تحتاج تركيزًا في الصباح، ويجمع المهام الصغيرة المتشابهة معًا، ويترك وقتًا لأوقات الصلاة والراحة. أخبرني بما يمكن تأجيله أو تفويضه.",
  "Here is my task list for today: [PASTE_LIST]. I have [NUMBER_OF_HOURS] working hours available and fixed commitments at [TIMES]. Sort the tasks with the Eisenhower matrix (urgent/important), then propose a schedule that puts deep-focus tasks in the morning, batches similar small tasks, and leaves time for prayer times and breaks. Tell me what can be postponed or delegated.",
  "لا تملأ اليوم بالكامل؛ اترك ساعة فارغة للأمور الطارئة.",
  "Don't fill the whole day — leave an hour free for the unexpected.")

P(s, "إجراء عمل موحد (SOP)", "Standard Operating Procedure (SOP)",
  "عندما تريد أن يؤدي أي موظف مهمة متكررة بنفس الطريقة.",
  "When you want any employee to do a recurring task the same way.",
  "حوّل هذا الشرح العشوائي لطريقة أداء مهمة [اسم المهمة] إلى إجراء عمل موحد (SOP): [اشرح المهمة بكلماتك]. التنسيق: الهدف، متى تُنفَّذ، من المسؤول، الأدوات المطلوبة، الخطوات مرقمة وواضحة (كل خطوة تبدأ بفعل)، الأخطاء الشائعة وكيف نتجنبها، وقائمة تحقق نهائية. اكتبه بلغة بسيطة يفهمها موظف جديد.",
  "Turn this rough explanation of how to do [TASK_NAME] into a standard operating procedure (SOP): [EXPLAIN_THE_TASK_IN_YOUR_OWN_WORDS]. Format: goal, when it's done, who's responsible, tools needed, clear numbered steps (each starting with a verb), common mistakes and how to avoid them, and a final checklist. Write in simple language a new employee can follow.",
  "سجّل شرحك صوتيًا وأنت تؤدي المهمة، ثم الصق التفريغ في الأمر بدل الكتابة.",
  "Record yourself explaining while doing the task, then paste the transcript instead of typing.")

P(s, "تحسين أي نص أو ترجمته", "Polish or Translate Any Text",
  "قبل نشر أو إرسال أي نص مهم.",
  "Before publishing or sending any important text.",
  "راجع هذا النص: [ألصق النص]. المطلوب: [صحّح الأخطاء الإملائية والنحوية فقط / حسّن الأسلوب مع الحفاظ على المعنى / ترجمه إلى الإنجليزية / ترجمه إلى العربية]. الجمهور: [الجمهور]. حافظ على المصطلحات وأسماء المنتجات كما هي. بعد النص المعدّل، اذكر في قائمة أهم التغييرات التي أجريتها ولماذا.",
  "Review this text: [PASTE_TEXT]. Task: [fix spelling and grammar only / improve style while keeping meaning / translate to English / translate to Arabic]. Audience: [AUDIENCE]. Keep terms and product names unchanged. After the edited text, list the main changes you made and why.",
  "في الترجمة إلى العربية اطلب «ترجمة طبيعية كأن كاتبها عربي» وليس ترجمة حرفية.",
  "When translating into Arabic, ask for \"a natural translation as if written by a native Arabic writer\", not a literal one.")

TOTAL = sum(len(x["prompts"]) for x in SECTIONS)
