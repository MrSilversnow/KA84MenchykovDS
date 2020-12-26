const EpamPage = require('./EpamPage');

describe('EPAM website testing', () => {
    const webdriver = require("selenium-webdriver"); 
    const driver = new webdriver.Builder().forBrowser("chrome").build();
    const epamPageObject = new EpamPage(webdriver, driver);

    beforeEach(function() {
        originalTimeout = jasmine.DEFAULT_TIMEOUT_INTERVAL;
        jasmine.DEFAULT_TIMEOUT_INTERVAL = 120000;
    });

    it('Menu should have a submenu', async () => {
         expect(await epamPageObject.clickOnMenuButton()).toEqual(true);
    });

    it('Search icon should open search form', async () => {
        expect(await epamPageObject.clickOnSearchIcon()).toEqual(true);
    });

    it('Epam icon shoould load main EPAM webpage', async () => {
        expect(await epamPageObject.clickOnEpamIcon()).toEqual('https://www.epam.com/');
    });

    it('Envelope icon should open ContactUs webpage', async () => {
        expect(await epamPageObject.clickOnEnvelopeIcon()).toEqual('https://www.epam.com/about/who-we-are/contact');
    });

    it('Hyperlinked text should open special webpages', async () => {
        expect(await epamPageObject.clickOnHyperlinkedText()).toContain('https://investors.epam.com/investors');
        expect(await epamPageObject.clickOnHyperlinkedText()).toContain('https://www.epam.com/web-accessibility-statement');
        expect(await epamPageObject.clickOnHyperlinkedText()).toContain('https://www.epam.com/cookie-policy');
        expect(await epamPageObject.clickOnHyperlinkedText()).toContain('https://www.epam.com/privacy-policy');
    });

    it('The special message appears when FirstName field is empty', async () => {
        expect(await epamPageObject.emptyFirstNameField()).toEqual(true);
    });

    it('Home button should return you to the home webpage', async () => {
        expect(await epamPageObject.clickOnHomeButton()).toEqual('https://www.epam.com/');
    });

    it('Language panel should open language submenu', async () => {
        expect(await epamPageObject.clickOnLanguagePanel()).toEqual(true);
    });
    afterEach(function() {        
        jasmine.DEFAULT_TIMEOUT_INTERVAL = originalTimeout;
    });
    
});