from config import PROJ, ADDRESS, CITY, POSTALCODE, COUNTRY, TELEPHONE, EMAIL, SITE, OPENINGHOURS, META_IMAGE, GOOGLE_META, UNDER_H, IMAGE_STARS, YOUTUBE_CHANEL, GOOGLE_RATING, GOOGLE_RATING_COUNT, YANDEX_RATING, YANDEX_RATING_COUNT

# Валидация shema - https://search.google.com/test/rich-results








def record_price(pricing_title: str, pricing_text: str, time: str, cost: str, cost_text: str) -> str:
    html = f"""
                                    <div class="price-row">
                                        <div class="price-cell">
                                            <span class="pricing-title">
                                                {pricing_title}
                                            </span>
                                            <br>
                                            <span class="pricing-text">
                                                {pricing_text}
                                            </span>
                                            <br>
                                            <span class="time">
                                                {time}
                                            </span>
                                        </div>
                                        <div class="price-cell-cost">
                                            <span class="cost">
                                                {cost}
                                            </span>
                                            <br>
                                            <span class="pricing-text">
                                                {cost_text}
                                            </span>
                                        </div>
                                    </div>
    """
    return html




def get_images(mini: str, alt: str, orig: str, title: str) -> str:
    html = f"""
    
                                <div class="col-sm-3 col-xs-6 wow fadeIn animated" data-wow-duration="300ms" data-wow-delay="100ms" style="visibility: visible; animation-duration: 300ms; animation-delay: 100ms; animation-name: fadeIn;">
                                    <div class="portfolio-wrapper">
                                        <div class="portfolio-single">
                                            <div class="portfolio-thumb">
                                                <img src="{mini}" class="img-responsive" alt="{alt}" title="{title}">
                                            </div>
                                            <div class="portfolio-view">
                                                <ul class="nav nav-pills">
                                                    <li><a href="{orig}" data-lightbox="example-set"><i class="fa fa-eye"></i></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="portfolio-info">
                                            <h3>{title}</h3>
                                        </div>
                                    </div>
                                </div>

    """
    return html







def get_html(data: dict) -> str:
    html_price = data.get("html_price") or ""
    keywords = data.get("keywords") or ""
    canonical = data.get("canonical") or ""
    content = data.get("content") or ""
    description = data.get("description") or ""
    image = data.get("image") or ""
    schema_html = data.get("schema_html") or ""
    title = data.get("title") or ""
    images = data.get("images") or ""
    h1 = data.get("h1") or ""
    img_title = data.get("img_title") or ""
    img_alt = data.get("img_alt") or ""
    message_under_table = data.get("message_under_table") or ""


    html = f"""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <meta property="og:url" content={canonical}>
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="website">
    <meta property="og:image" content="{META_IMAGE}">
    <link rel="canonical" href="{canonical}">

    <meta name="google-site-verification" content="{GOOGLE_META}" />
    <title>{title}</title>
    <meta name="keywords" content="{keywords}" />
	<meta name="description" content="{description}" />

    <?php include "./jski.html" ?>

</head><!--/head-->

<body oncopy="return false;">

    <div id="main-content">

        <header id="header">
            <?php include "./header.html" ?>
            <div style="width:100%; height:30px;"></div>
            <section id="page-breadcrumb">
                <div class="vertical-center sun">
                    <div class="container">
                        <div class="row">
                            <div class="action">
                                <div class="col-sm-12">
                                    <h1>{h1}<a class="stars-youtube" href="#5stars"><img class="stars" title="Отзывы" src="{IMAGE_STARS}"></a><span class="stars-youtube" data-link="{YOUTUBE_CHANEL}" onclick="window.location=this.getAttribute('data-link')"><i class="fa fa-youtube"></i></span></h1>
                                    <span>{UNDER_H}</span>
                                    <img title="{img_title}" alt="{img_alt}" src="{image}" class="img-h">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </header>


        <main>
            <section id="company-information" class="choose">
                <article>
                    <div class="container">
                        <div class="row">
                            <!-- col-sm-12 /-->
                            <div class="col-sm-6 wow fadeInDown animated" data-wow-duration="500ms" data-wow-delay="0ms" style="visibility: visible; animation-duration: 500ms; animation-delay: 0ms; animation-name: fadeInDown;">

                                <div class="price-table">
                                    <!-- Заголовки -->
                                    <div class="price-row price-header">
                                        <div class="price-cell">
                                            Услуга
                                        </div>
                                        <div class="price-cell-cost">
                                            Цена
                                        </div>
                                    </div>
                                    {html_price}


                                    <div class="inline-table">
                                        <span class="inline-table">* Пожалуйста, предупредите о своем приходе заранее</span>
                                        <br>
                                        <span class="inline-table">{message_under_table}</span>
                                    </div>


                                </div> <!-- price-table /-->
                                <br>

                            </div> <!-- col-sm-6 /-->
                            <div class="col-sm-6 padding-top wow fadeInDown animated" data-wow-duration="500ms" data-wow-delay="0ms" style="visibility: visible; animation-duration: 500ms; animation-delay: 0ms; animation-name: fadeInDown;">

                                <div class="content">

                                    {content}

                                </div> <!-- content /-->
                                <br>

                            </div> <!-- col-sm-6 /-->
                        </div> <!-- row /-->



                    <br>
                    <br>


                    <section id="recent-projects" class="recent-projects">
                        <div class="container">
                            <div class="row">
                                <!--<h2 class="title wow fadeInDown animated" data-wow-duration="300ms" data-wow-delay="100ms" style="visibility: visible; animation-duration: 300ms; animation-delay: 100ms; animation-name: fadeInDown;">Примеры починки ноутбуков:</h2>/-->
                                <!-- <p class="padding-bottom wow fadeInDown animated" data-wow-duration="200ms" data-wow-delay="200ms" style="visibility: visible; animation-duration: 200ms; animation-delay: 200ms; animation-name: fadeInDown;"></p> -->

                                {images}

                            </div> <!-- row /-->
                        </div> <!-- container /-->
                    </section>
                    <!--imggalery-->



                    </div> <!-- container /-->
                </article>
            </section>
        </main>



        <footer id="footer">
        <?php include "./footer.html" ?>
        </footer>



    </div><!-- main-content /-->

<script type="application/ld+json">
    {schema_html}
</script>

</body>
</html>
    """
    return html






def get_schema_html(page: str, serv_name: str, h1_title: str, url: str, description: str) -> dict:

    if page == "index":
        schem = {
            "@context": "https://schema.org",
            "@type": "ProfessionalService",
            "@id": "https://www.1rmaster.ru/#provider",
            "name": "1rmaster",
            "description": "Профессиональный ремонт ноутбуков в Москве рядом с метро Первомайская. Опыт более 15 лет, гарантия на работы до 6 месяцев.",
            "image": "https://www.1rmaster.ru/images/logo-2.0.webp",
            "priceRange": "RUB",
            "url": "https://www.1rmaster.ru/",
            "telephone": "+79998329934",
            "email": "1rmaster@mail.ru",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "3-я Парковая улица, 38",
                "addressLocality": "Москва",
                "postalCode": "105425",
                "addressCountry": "RU"
            },
            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": YANDEX_RATING,
                "bestRating": "5",
                "ratingCount": YANDEX_RATING_COUNT
            },
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": 55.801931,
                "longitude": 37.782728
            },
            # "openingHours": ["Mo-Fr 11:00-19:00", "Sa 11:00-19:00"],

            "openingHoursSpecification": [
                {
                    "@type": "OpeningHoursSpecification",
                    "dayOfWeek": [
                        "Monday",
                        "Tuesday",
                        "Wednesday",
                        "Thursday",
                        "Friday",
                        "Saturday"
                    ],
                    "opens": "11:00",
                    "closes": "19:00"
                }
            ],

            "hasOfferCatalog": {
                "@type": "OfferCatalog",
                "name": serv_name,
                "itemListElement": []
            }
        }

    else:

        schem = {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": h1_title,
            "description": description,
            "url": url,
            "provider": {
                "@type": "ProfessionalService",
                "@id": "https://www.1rmaster.ru/#provider",
                "name": "1rmaster",
                "priceRange": "RUB",
                "telephone": "+79998329934",
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": "3-я Парковая улица, 38",
                    "addressLocality": "Москва",
                    "postalCode": "105425",
                    "addressCountry": "RU"
                },
                "image": "https://www.1rmaster.ru/images/logo-2.0.webp"
            },
            "areaServed": {
                "@type": "Place",
                "name": "Москва, ВАО, м. Первомайская",
            },
            "offers": []
        }

    return schem






