from config import PROJ, ADDRESS, CITY, POSTALCODE, COUNTRY, TELEPHONE, EMAIL, SITE, OPENINGHOURS, META_IMAGE, GOOGLE_META, UNDER_H, IMAGE_STARS, YOUTUBE_CHANEL, GOOGLE_RATING, GOOGLE_RATING_COUNT, YANDEX_RATING, YANDEX_RATING_COUNT









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
                                                <img src="{mini}" class="img-responsive" alt="{alt}">
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






def get_schema_html(page: str, serv_name: str, h1_title: str, url: str, description: str, servicetype: str) -> dict:

    if page == "index":
        schem = {
            "@context": "https://schema.org",
            "@type": "LocalBusiness",
            "name": "1rmaster - Ремонт ноутбуков",
            "description": "Срочный и профессиональный ремонт ноутбуков в Москве у метро Первомайская. Опыт 15+ лет, гарантия до полугода.",
            "image": "https://www.1rmaster.ru/images/logo-2.0.webp",
            "priceRange": "1000-3800₽",
            "url": "https://www.1rmaster.ru/",
            "telephone": "+79998329934",
            "email": "1rmaster@mail.ru",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "улица 3-я Парковая, дом 38",
                "addressLocality": "Москва",
                "postalCode": "105425",
                "addressCountry": "RU"
            },
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": "55.801931",
                "longitude": "37.782728"
            },
            "openingHours": ["Mo-Fr 11:00-19:00", "Sa 11:00-19:00"],

            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": 4.7,
                "reviewCount": 277,
                "bestRating": 5,
                "worstRating": 1
            },
            "review": [
                {
                    "@type": "Review",
                    "author": {
                        "@type": "Organization",
                        "name": "Google"
                    },
                    "reviewRating": {
                        "@type": "Rating",
                        "ratingValue": GOOGLE_RATING,
                        "bestRating": 5,
                        "worstRating": 1
                    }
                },
                {
                    "@type": "Review",
                    "author": {
                        "@type": "Organization",
                        "name": "Yandex"
                    },
                    "reviewRating": {
                        "@type": "Rating",
                        "ratingValue": YANDEX_RATING,
                        "bestRating": 5,
                        "worstRating": 1
                    }
                },
                {
                    "@type": "Review",
                    "author": {"@type": "Person", "name": "Егор Паталах"},
                    "reviewRating": {
                        "@type": "Rating",
                        "ratingValue": 5,
                        "bestRating": 5,
                        "worstRating": 1
                    },
                    "datePublished": "2025-07-31",
                    "reviewBody": "Обращался за ремонтом ноутбука. Все очень оперативно и по делу. Мастер всегда на связи, описал весь процесс ремонта с фотоотчетом. Супер удобно и рядом на районе."
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
            "serviceType": servicetype,
            "provider": {
                "@type": "LocalBusiness",
                "name": "1rmaster",
                "url": "https://www.1rmaster.ru",
                "telephone": "+79998329934"
            },
            "areaServed": {
                "@type": "City",
                "name": "Москва"
            },
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": "55.801931",
                "longitude": "37.782728"
            },
            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": "4.7",
                "reviewCount": "277",
            "bestRating": "5",
            "worstRating": "1"
            },
            "review": [
                {
                    "@type": "Review",
                    "author": {
                        "@type": "Organization",
                        "name": "Google"
                    },
                    "reviewRating": {
                        "@type": "Rating",
                        "ratingValue": GOOGLE_RATING,
                        "bestRating": "5",
                        "worstRating": "1"
                    },
                    "reviewCount": GOOGLE_RATING_COUNT
                },
                {
                    "@type": "Review",
                    "author": {
                        "@type": "Organization",
                        "name": "Yandex"
                    },
                    "reviewRating": {
                        "@type": "Rating",
                        "ratingValue": YANDEX_RATING,
                        "bestRating": "5",
                        "worstRating": "1"
                    },
                    "reviewCount": YANDEX_RATING_COUNT
                }
            ],
            "offers": []
        }

    return schem

















# def get_schema():
#
#     ff = {
#         "@context": "https://schema.org",
#         "@type": "Service",
#         "serviceType": "Ремонт ноутбуков в Москве",
#         "provider": {
#             "@type": "LocalBusiness",
#             "name": "1rmaster",
#             "address": {
#                 "@type": "PostalAddress",
#                 "streetAddress": "улица 3-я Парковая, дом 38",
#                 "addressLocality": "Москва",
#                 "addressRegion": "Москва",
#                 "postalCode": "105425",
#                 "addressCountry": "Россия"
#             },
#             "telephone": "+79998329934",
#             "email": " 1rmaster@mail.ru",
#             "url": "https://www.1rmaster.ru",
#             "openingHours": "Su-Fr 11:00-19:00"
#         },
#         "description": "Ремонт нутбуков, чистка, замена матрицы, диска и ремонт сложных ситуаций. Гарантия.",
#         "areaServed": {
#             "@type": "AdministrativeArea",
#             "name": "Москва"
#         },
#         "hasOfferCatalog": {
#             "@type": "OfferCatalog",
#             "name": "Услуги по ремонту ноутбуков",
#             "itemListElement": [
#                 {
#                     "@type": "Offer",
#                     "itemOffered": {
#                         "@type": "Service",
#                         "name": "Чистка системы охлаждения и замена термопасты",
#                         "description": "Чистка системы охлаждения и замена термопасты на пасту с фазовым переходом при клиенте",
#                         "price": "2000",
#                         "priceCurrency": "RUB"
#                     }
#                 },
#                 {
#                     "@type": "Offer",
#                     "itemOffered": {
#                         "@type": "Service",
#                         "name": "Замена матрицы",
#                         "description": "Замена матрицы на ноутбуке + стоимость матрицы",
#                         "price": "2000",
#                         "priceCurrency": "RUB"
#                     }
#                 }
#             ]
#         }
#     }