import asyncio
from playwright.async_api import async_playwright

async def search_vitrinelinguistique(query):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://vitrinelinguistique.oqlf.gouv.qc.ca/")

        # Type the query into the search input field
        await page.type("#searchBannerField", query)

        # Click the search button
        await page.click(".search-banner__submit")

        # Extract information from each search result or return an empty array if no results are found
        results = await page.evaluate('''() => {
                    const noResultMessage = document.querySelector('.search-results-title');
                    if (noResultMessage && noResultMessage.innerText.includes("Aucun résultat")) {
                        return [];
                    }

                    const resultItems = document.querySelectorAll('.search-results__item');
                    const resultData = [];

                    resultItems.forEach((item) => {
                        const titleElement = item.querySelector('.result__title strong');
                        const linkElement = item.querySelector('.result__title a');
                        const summaryElement = item.querySelector('.result__summary');
                        const domainElements = item.querySelectorAll('.result__domaines small');

                        if (titleElement && linkElement && summaryElement && domainElements) {
                            const term = titleElement.innerText.trim();
                            const link = "https://vitrinelinguistique.oqlf.gouv.qc.ca/" + linkElement.getAttribute('href').trim();
                            const description = summaryElement.innerText.trim();
                            const domains = Array.from(domainElements).map(domain => domain.innerText.trim());

                            resultData.push({ term, link, description, domains });
                        }
                    });

                    return resultData;
                }''')

        # # Print the list of JSON objects
        # for result in results:
        #     print(result)

        # Close the browser
        await browser.close()
        return results
    
# async def main():
#
#     # add in other UI elements here e.g. title, input data etc
#     query_string = "business"
#     results = await search_vitrinelinguistique(query_string)
#     results = await search_termium(query_string)
#     # print(results)
#     st.write(results)
 

# if __name__ == '__main__':
#     loop = asyncio.ProactorEventLoop()
#     loop.run_until_complete(main())