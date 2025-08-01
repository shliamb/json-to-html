


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







def get_html(data: dict) -> str:
    html_price = data.get("html_price")
    keywords = data.get("keywords")
    canonical = data.get("canonical")
    content = data.get("content")
    description = data.get("description")
    image = data.get("image")
    schema_html = data.get("schema_html")
    title = data.get("title")

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
    <meta property="og:image" content="https://www.1rmaster.ru/images/1rmaster.png">
    <link rel="canonical" href="{canonical}">

    <meta name="google-site-verification" content="s8VFYPjHsP5eOA84WBV2AurAn6ha6iWX5d5G82Y_RzE" />
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
                                    <h1>Ремонт ноутбуков <a class="stars-youtube" href="#5stars"><img class="stars" title="Отзывы" src="/images/main/5stars.webp"></a><span class="stars-youtube" data-link="https://www.youtube.com/@onermaster" onclick="window.location=this.getAttribute('data-link')"><i class="fa fa-youtube"></i></span></h1>
                                    <span>Москва • Щёлковская • Первомайская • Измайловская</span>
                                    <img title="Ремонт ноутбуков в Москве" alt="Срочный ремонт ноутбуков в Москве с гарантией" src="{image}" class="img-h">
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
                                        <span class="inline-table">** При предъявлении студенческого билета, сделаю скидку 10%.</span>
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

                                <div class="col-sm-3 col-xs-6 wow fadeIn animated" data-wow-duration="500ms" data-wow-delay="100ms" style="visibility: visible; animation-duration: 500ms; animation-delay: 100ms; animation-name: fadeIn;">
                                    <div class="portfolio-wrapper">
                                        <div class="portfolio-single">
                                            <div class="portfolio-thumb">
                                                <img src="images/laptop/mlaptop1.webp" class="img-responsive" alt="Замена процессора intel ">
                                            </div>
                                            <div class="portfolio-view">
                                                <ul class="nav nav-pills">
                                                    <li><a href="images/laptop/laptop1.jpg" data-lightbox="example-set"><i class="fa fa-eye"></i></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="portfolio-info">
                                            <h3>Перепайка CPU <!--<a target="_blank" href="https://www.instagram.com/p/Cl1fLH7LoXJ/"><button type="button" class="btn btn-xs btn-default">подробнее</button></a>/--></h3>
                                        </div>
                                    </div>
                                </div>

                                <div class="col-sm-3 col-xs-6 wow fadeIn animated" data-wow-duration="300ms" data-wow-delay="100ms" style="visibility: visible; animation-duration: 300ms; animation-delay: 100ms; animation-name: fadeIn;">
                                    <div class="portfolio-wrapper">
                                        <div class="portfolio-single">
                                            <div class="portfolio-thumb">
                                                <img src="images/laptop/mlaptop2.webp" class="img-responsive" alt="Замена процессора Ryzen">
                                            </div>
                                            <div class="portfolio-view">
                                                <ul class="nav nav-pills">
                                                    <li><a href="images/laptop/laptop2.jpg" data-lightbox="example-set"><i class="fa fa-eye"></i></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="portfolio-info">
                                            <h3>Смена Ryzen <!--<a target="_blank" href="https://www.instagram.com/p/CiCkKSZLiD2/"><button type="button" class="btn btn-xs btn-default">подробнее</button></a>/--></h3>
                                        </div>
                                    </div>
                                </div>

                                <div class="col-sm-3 col-xs-6 wow fadeIn animated" data-wow-duration="300ms" data-wow-delay="100ms" style="visibility: visible; animation-duration: 300ms; animation-delay: 100ms; animation-name: fadeIn;">
                                    <div class="portfolio-wrapper">
                                        <div class="portfolio-single">
                                            <div class="portfolio-thumb">
                                                <img src="images/laptop/mlaptop3.webp" class="img-responsive" alt="Восстановление маски после сервиса">
                                            </div>
                                            <div class="portfolio-view">
                                                <ul class="nav nav-pills">
                                                    <li><a href="images/laptop/laptop3.jpg" data-lightbox="example-set"><i class="fa fa-eye"></i></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="portfolio-info">
                                            <h3>Реставрация маски <!--<a target="_blank" href="https://www.instagram.com/p/CmHfmFtL4eU/"><button type="button" class="btn btn-xs btn-default">подробнее</button></a>/--></h3>
                                        </div>
                                    </div>
                                </div>

                                <div class="col-sm-3 col-xs-6 wow fadeIn animated" data-wow-duration="300ms" data-wow-delay="100ms" style="visibility: visible; animation-duration: 300ms; animation-delay: 100ms; animation-name: fadeIn;">
                                    <div class="portfolio-wrapper">
                                        <div class="portfolio-single">
                                            <div class="portfolio-thumb">
                                                <img src="images/laptop/mlaptop4.webp" class="img-responsive" alt="Чистка ноутбука">
                                            </div>
                                            <div class="portfolio-view">
                                                <ul class="nav nav-pills">
                                                    <li><a href="images/laptop/laptop4.jpg" data-lightbox="example-set"><i class="fa fa-eye"></i></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="portfolio-info">
                                            <h3>Очистка <!--<a target="_blank" href="https://www.instagram.com/p/Cd0PLCGMr28/"><button type="button" class="btn btn-xs btn-default">подробнее</button></a>/--></h3>
                                        </div>
                                    </div>
                                </div>

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


{schema_html}

</body>
</html>
    """
    return html


def get_schema_html(serv_name: str, title: str, url: str, description: str) -> dict:
    schem = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": title,
        "url": url,  # // Уникальный!
        "description": description,
        "provider": {
            "@type": "LocalBusiness",
            "name": "1rmaster",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "улица 3-я Парковая, дом 38",
                "addressLocality": "Москва",
                "addressRegion": "Москва",
                "postalCode": "105425",
                "addressCountry": "Россия"
            },
            "telephone": "+79998329934",
            "email": " 1rmaster@mail.ru",
            "url": "https://www.1rmaster.ru", # // Общий
            "openingHours": "Su-Fr 11:00-19:00"
        },
        "areaServed": {
            "@type": "AdministrativeArea",
            "name": "Москва"
        },
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": serv_name, #"Услуги по ремонту ноутбуков",
            "itemListElement": []

        }
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