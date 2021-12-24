from playwright.sync_api import Playwright, sync_playwright
from time import sleep

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://public.tableau.com/app/profile/karon5500/viz/moph_covid_v3/Story1
    page.goto("https://public.tableau.com/app/profile/karon5500/viz/moph_covid_v3/Story1")

    page.wait_for_timeout(4000)
    # page.wait_for_load_state('domcontentloaded')
    # while True:
    #     if page.frame(url="https://public.tableau.com/views/moph_covid_v3/Story1?%3Adisplay_static_image=y&%3AbootstrapWhenNotified=true&%3Aembed=true&%3Alanguage=en-US&:embed=y&:showVizHome=n&:apiID=host0#navType=0&navSrc=Parse") is not None:
    #         break
    #     sleep(1)

    # Click .tabFlipboardNavPoints span:nth-child(2) .tabStoryPointCaption
    page.frame(url="https://public.tableau.com/views/moph_covid_v3/Story1?%3Adisplay_static_image=y&%3AbootstrapWhenNotified=true&%3Aembed=true&%3Alanguage=en-US&:embed=y&:showVizHome=n&:apiID=host0#navType=0&navSrc=Parse").click(".tabFlipboardNavPoints span:nth-child(2) .tabStoryPointCaption")
    page.wait_for_load_state('networkidle')

    print('waited')
    sleep(10)
    # Click [aria-label="นครราชสีมา, Prov Name. Press Space to toggle selection. Press Escape to go back to the left margin. Use arrow keys to navigate headers"]
    # page.frame(url="https://public.tableau.com/views/moph_covid_v3/Story1?%3Adisplay_static_image=y&%3AbootstrapWhenNotified=true&%3Aembed=true&%3Alanguage=en-US&:embed=y&:showVizHome=n&:apiID=host0#navType=0&navSrc=Parse").click("[aria-label=\"นครราชสีมา, Prov Name. Press Space to toggle selection. Press Escape to go back to the left margin. Use arrow keys to navigate headers\"]")

    # # Click [aria-label="สุรินทร์, Prov Name. Press Space to toggle selection. Press Escape to go back to the left margin. Use arrow keys to navigate headers"]
    # page.frame(url="https://public.tableau.com/views/moph_covid_v3/Story1?%3Adisplay_static_image=y&%3AbootstrapWhenNotified=true&%3Aembed=true&%3Alanguage=en-US&:embed=y&:showVizHome=n&:apiID=host0#navType=0&navSrc=Parse").click("[aria-label=\"สุรินทร์, Prov Name. Press Space to toggle selection. Press Escape to go back to the left margin. Use arrow keys to navigate headers\"]")

    # # Click [aria-label="กรุงเทพมหานคร, Prov Name. Press Space to toggle selection. Press Escape to go back to the left margin. Use arrow keys to navigate headers"]
    # page.frame(url="https://public.tableau.com/views/moph_covid_v3/Story1?%3Adisplay_static_image=y&%3AbootstrapWhenNotified=true&%3Aembed=true&%3Alanguage=en-US&:embed=y&:showVizHome=n&:apiID=host0#navType=0&navSrc=Parse").click("[aria-label=\"กรุงเทพมหานคร, Prov Name. Press Space to toggle selection. Press Escape to go back to the left margin. Use arrow keys to navigate headers\"]")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
