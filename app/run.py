import re
import json
from config import INPUT_DATA, OUTPUT_DATA
from html import record_price, get_html, get_schema_html




def extract_digits_after_r(text: str):
    match = re.search(r'[Rр₽](\d+)', text)
    return match.group(1) if match else None


def main():
    error_html = 0
    successful_html = 0

    try:

        with open(f"{INPUT_DATA}data.json", "r") as file:
            data_in_json = json.load(file)

        for page, values in data_in_json.items():

            canonical = values.get("canonical")
            title = values.get("title")
            serv_name = values.get("serv_name")
            description = values.get("description")

            schema_html = get_schema_html(serv_name, title, canonical, description)

            html_price = ""
            price = values.get("price")
            if price:
                for bit_price in price:

                    pricing_title = bit_price.get("pricing-title") or ""
                    pricing_text = bit_price.get("pricing-text") or ""
                    time = bit_price.get("time") or ""
                    cost = bit_price.get("cost") or ""
                    cost_text = bit_price.get("cost-text") or ""

                    offer = {
                        "@type": "Offer",
                        "itemOffered": {
                            "@type": "Service",
                            "name": pricing_title,
                            "description": pricing_text,
                            "price": extract_digits_after_r(cost),
                            "priceCurrency": "RUB"
                        }
                    }
                    schema_html["hasOfferCatalog"]["itemListElement"].append(offer)

                    row_price_html = record_price(pricing_title, pricing_text, time, cost, cost_text)
                    html_price += row_price_html

            data = {
                "html_price": html_price,
                "content": values.get("content"),
                "canonical": canonical,
                "keywords": ", ".join(values["keywords"]) if values.get("keywords") else "",
                "description": description,
                "image": values.get("image"),
                "schema_html": json.dumps(schema_html, ensure_ascii=False, indent=4),
                "title": title

            }
            html_final = get_html(data)
            if html_final:
                successful_html += 1
                with open(f"{OUTPUT_DATA}{page}.html", "w") as file:
                    file.write(html_final)
            else:
                error_html += 1

        print(f"Done. Successful page:{successful_html}, error page: {error_html}")

    except Exception as e:
        print(f"Error: {e}, successful page:{successful_html}, error page: {error_html}")
        return




if __name__ == "__main__":
    main()