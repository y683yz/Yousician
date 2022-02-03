#!/usr/bin/python
# By Yongzhao Yang 2022.01.25

BROWSER = "chromium"
HEADLESS = "True"
LOCALE = "en-GB"


def main():
    with sync_playwright() as playwright:
        browser = "playwright.{}.launch(headless={})".format(BROWSER, HEADLESS)
        browser = eval(browser)
        context = browser.new_context(viewport={'width': 2040, 'height': 1060}, locale=LOCALE)
        page = context.new_page()
        # replace spaces in the string with wed-safe %20 and remove prefix and postfix
        song = quote(str(sys.argv[1:])[1:-1])[3:-3]
        print("Searching: " + song.replace('%20', ' ') + '\n')
        url = 'https://yousician.com/songs/search/%s' % song
        try:
            page.goto(url)
        except ConnectionError as e:
            print(e)
            raise e
        locator = page.locator('a[href*="/songs/"]')
        s = locator.count()
        if not s:       # s is not empty
            print("No song about <" + song + "> was found")
        else:
            playlist = {}
            for i in range(s):
                item = locator.nth(i).all_inner_texts()[0].split('\n\n')
                # save results to a dict
                playlist[item[0]] = item[1]

            # Output sorted dict as a list with tuples
            print(sorted(playlist.items(), key=my_key, reverse=False))
        

def my_key(t):
    """ Customize your sorting logic using this function.  The parameter to
    this function is a tuple.  Comment/uncomment the return statements to test
    different logics.
    """
    # return t[1]              # sort by artist names of the songs
    return t[1], t[0]       # sort by artist names, then by the songs
    # return len(t[0])        # sort by length of the songs
    # return t[0][-1]         # sort by last character of the songs


if __name__ == '__main__':
    import sys
    from playwright.sync_api import sync_playwright
    from urllib.parse import quote
    main()

