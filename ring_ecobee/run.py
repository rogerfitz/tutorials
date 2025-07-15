import asyncio
from playwright.async_api import async_playwright
import email
import imaplib
from config import ECOBEE_EMAIL, ECOBEE_PASSWORD, EMAIL_USER, EMAIL_PASSWORD


async def set_ecobee(away=False):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=1000)
        page = await browser.new_page()
        await page.goto("https://auth.ecobee.com/u/login/")

        await page.fill("#username", ECOBEE_EMAIL)
        await page.get_by_role("button", name="Continue").click()
        await page.fill("#password", ECOBEE_PASSWORD)
        await page.get_by_role("button", name="Sign in").click()

        # TODO 2FA -- nope skipping just contact support to remove it

        # TODO Select thermostat and update to away
        await page.wait_for_selector('span:text("My Home")', timeout=15000)
        tiles = await page.locator('div[data-qa-class="thermostat-tile"]').all()

        for i, tile in enumerate(tiles):
            await tile.click()
            await page.wait_for_timeout(1100)

            if away:
                await page.click("text=Away and hold")
            else:
                await page.click("text=and holding")
            await page.wait_for_timeout(1000)
            await page.go_back(timeout=15000)
            await page.wait_for_timeout(1000)

            print(f"✅ Set Ecobee {i}")



async def run():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL_USER,  EMAIL_PASSWORD)
    mail.select("inbox")
    status, data = mail.search(None, '(UNSEEN SUBJECT "Ring Alarm is")')
    email_ids = data[0].split()
    email_ids.reverse()

    for eid in email_ids:
        _, msg_data = mail.fetch(eid, "(RFC822)")
        raw_msg = msg_data[0][1]
        msg = email.message_from_bytes(raw_msg)

        subject = msg["subject"]
        print(f"✅ Found Ring Email: {subject}")
        if "Disarmed" in subject:
            await set_ecobee(away=False)
        elif "Away" in subject:
            await set_ecobee(away=True)
        # mark as read
        mail.store(eid, '+FLAGS', '\\Seen')
        break



asyncio.run(run())
