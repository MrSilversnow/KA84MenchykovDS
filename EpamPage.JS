const BasePage = require('./BasePage');
 

class EpamPage extends BasePage {
    constructor(webdriver, driver, timeout = 10000) {
        super(webdriver, driver, timeout);
        this.URL = {
            'EPAM_URL': 'https://www.epam.com/',
            'EPAM_CONTACT_URL': 'https://www.epam.com/about/who-we-are/contact'
        };
        this.SUBMENU_XPATH = {
            "SERVICES": '/html/body/div[2]/div[2]/div[1]/header/div/div/nav/ul/li[1]/a',
            "HOW_WE_DO_IT": '/html/body/div[2]/div[2]/div[1]/header/div/div/nav/ul/li[2]/a',
            "OUR_WORK": '/html/body/div[2]/div[2]/div[1]/header/div/div/nav/ul/li[3]/a',
            "INSIGHTS": '/html/body/div[2]/div[2]/div[1]/header/div/div/nav/ul/li[4]/a',
            "ABOUT": '/html/body/div[2]/div[2]/div[1]/header/div/div/nav/ul/li[5]/a',
            "CAREERS": '/html/body/div[2]/div[2]/div[1]/header/div/div/nav/ul/li[6]/a',
            "LANGUAGE": '/html/body/div[2]/div[2]/div[1]/header/div/div/nav/div'
        };
        this.HT_XPATH = {
            "INVESTORS": {
                'XPATH': '/html/body/div[2]/div[3]/div[1]/footer/div/div[2]/ul[1]/li[1]/a',
                'LINK': 'https://investors.epam.com/investors'
            },
            "WEB_ACCESSIBILITY": {
                'XPATH': '/html/body/div[2]/div[3]/div[1]/footer/div/div[2]/ul[1]/li[6]/a',
                'LINK': 'https://www.epam.com/web-accessibility-statement'
            },
            "COOKIE POLICY": {
                'XPATH': '/html/body/div[2]/div[3]/div[1]/footer/div/div[2]/ul[1]/li[4]/a',
                'LINK': 'https://www.epam.com/cookie-policy'
            },
            "PRIVACY POLICY": {
                'XPATH': '/html/body/div[2]/div[3]/div[1]/footer/div/div[2]/ul[1]/li[3]/a',
                'LINK': 'https://www.epam.com/privacy-policy'
            }
        }
        this.LANGUAGE_XPATH = {
            "00": '/html/body/div[2]/div[2]/div[1]/header/div/ul/li[2]/div/nav/ul/li[1]/a',
            "01": '/html/body/div[2]/div[2]/div[1]/header/div/ul/li[2]/div/nav/ul/li[4]/a',
            "02": '/html/body/div[2]/div[2]/div[1]/header/div/ul/li[2]/div/nav/ul/li[7]/a',
            "03": '/html/body/div[2]/div[2]/div[1]/header/div/ul/li[2]/div/nav/ul/li[10]/a',
            "04": '/html/body/div[2]/div[2]/div[1]/header/div/ul/li[2]/div/nav/ul/li[2]/a',
            "05": '/html/body/div[2]/div[2]/div[1]/header/div/ul/li[2]/div/nav/ul/li[5]/a',
            "06": '/html/body/div[2]/div[2]/div[1]/header/div/ul/li[2]/div/nav/ul/li[8]/a',
            "07": '/html/body/div[2]/div[2]/div[1]/header/div/ul/li[2]/div/nav/ul/li[3]/a',
            "08": '/html/body/div[2]/div[2]/div[1]/header/div/ul/li[2]/div/nav/ul/li[6]/a',
            "09": '/html/body/div[2]/div[2]/div[1]/header/div/ul/li[2]/div/nav/ul/li[9]/a'
        }
        
    }

    async clickOnMenuButton(sleepFor = 2500) {
        let indx;
        await this.driver.get("https://www.epam.com/");
        await this.driver.manage().window().setSize(640, 480);
        let menu = await this.driver.findElement(this.webdriver.By.className("hamburger-menu__button"));
        await this.click(menu);
        for(indx in this.SUBMENU_XPATH) {
            await this.elementIsVisibleByXPath(this.SUBMENU_XPATH[indx]);        
        }
        await this.driver.sleep(sleepFor);
        return true;
    }

    async clickOnSearchIcon(sleepFor = 2500) {
        await this.driver.get("https://www.epam.com/");
        await this.driver.manage().window().setSize(640, 480);
        let searchIcon = await this.driver.findElement(this.webdriver.By.className("header-search__button header__icon")); 
        await this.click(searchIcon);
        await this.elementIsVisibleByXPath('/html/body/div[2]/div[2]/div[1]/header/div/ul/li[3]/div/div')
        await this.driver.sleep(sleepFor);
        return true;
    }

    async clickOnEpamIcon(sleepFor = 2000) {
        await this.driver.get("https://www.epam.com/");
        await this.driver.manage().window().maximize();
        let searchIcon = await this.driver.findElement(this.webdriver.By.className("header__logo")); 
        await this.click(searchIcon);
        await this.driver.sleep(sleepFor);
        let result = await this.getCurrentUrl();
        return result;
    }

    async clickOnEnvelopeIcon(sleepFor = 2000) {
        await this.driver.get("https://www.epam.com/");
        let envelopeIcon = await this.driver.findElement(this.webdriver.By.className("cta-button-ui cta-button--envelope header__control")); 
        await this.click(envelopeIcon);
        await this.driver.sleep(sleepFor)
        let result = await this.getCurrentUrl();
        return result;
    }

    async clickOnHyperlinkedText(sleepFor = 1500) {
        await this.driver.get("https://www.epam.com/");
        await this.driver.manage().window().maximize();
        let indx, result = [];
        for(indx in this.HT_XPATH) {            
            await this.driver.sleep(sleepFor);
            await this.clickByXPath(this.HT_XPATH[indx].XPATH);
            await this.driver.sleep(sleepFor);
            result.push(await this.getCurrentUrl());
            await this.driver.get("https://www.epam.com/"); 
            await this.driver.sleep(sleepFor);                      
        }
        return result;
    }
    
    async emptyFirstNameField(sleepFor = 1500) {
        await this.driver.get("https://www.epam.com/about/who-we-are/contact");
        await this.driver.manage().window().maximize();
        await this.clickByXPath('/html/body/div[2]/main/div[1]/div[1]/section/div/div[6]/div/form/div[3]/div/div[2]/button');
        await this.driver.sleep(sleepFor);
        await this.clickByXPath('/html/body/div[2]/main/div[1]/div[1]/section/div/div[6]/div/form/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/input');
        await this.elementIsVisibleByXPath('/html/body/div[2]/main/div[1]/div[1]/section/div/div[6]/div/form/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/span');
        await this.driver.sleep(sleepFor)
        return true;
    }

    async clickOnHomeButton(sleepFor = 2500) {
        await this.driver.get("https://www.epam.com/about/who-we-are/contact");
        await this.driver.manage().window().maximize();
        await this.driver.sleep(sleepFor);
        await this.clickByXPath('/html/body/div[2]/div[2]/div[2]/div/div/nav/ol/li[1]/a', 10000);
        await this.driver.sleep(sleepFor);
        let result = await this.getCurrentUrl();
        return result;
    }

    async clickOnLanguagePanel(sleepFor = 1500) {
        await this.driver.get("https://www.epam.com/");
        await this.driver.manage().window().maximize();
        let indx;
        this.driver.sleep(sleepFor);
        await this.click(this.driver.findElement(this.webdriver.By.className("location-selector__button")));        
        for(indx in this.LANGUAGE_XPATH) {
            await this.elementIsVisibleByXPath(this.LANGUAGE_XPATH[indx]);
            this.driver.sleep(sleepFor);
        }
    await this.driver.sleep(sleepFor);
    return true;    
    }
}


module.exports = EpamPage;








const webdriver = require("selenium-webdriver"); 
let driver = new webdriver.Builder().forBrowser("chrome").build();
let epamPage = new EpamPage(webdriver, driver);
//epamPage.clickOnMenuButton();  // Check.
//epamPage.clickOnSearchIcon();  // Check.
//epamPage.clickOnEpamIcon();  // Check.
//epamPage.clickOnEnvelopeIcon();  // Check.
epamPage.clickOnHyperlinkedText(); // Check.
//epamPage.emptyFirstNameField(); // Check.
//epamPage.clickOnHomeButton(); // Check.
//epamPage.clickOnLanguagePanel(); // Check.