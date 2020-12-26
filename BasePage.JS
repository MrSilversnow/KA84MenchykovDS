'use strict';


class BasePage {
    constructor(webdriver, driver, timeout = 5000) {        
        this.timeout = timeout;
        this.driver = driver;
        this.webdriver = webdriver;
    }

    async quit() {
        await this.driver.quit();
    }

    async get(url) {
        await this.driver.get(url);
    }

    async getCurrentUrl() {
        return await this.driver.getCurrentUrl();
    }

    async wait(selector, elementName, timeout = 15000) {
        let result;
        await this.driver.wait(
            () =>
                this.driver.findElement(selector).then(
                    (element) => {
                        result = element;
                        return true;
                    },
                    (err) => {
                        if (err.name === "NoSuchElementError") {
                            return false;
                        }
                        return true;
                    }
                ),
            timeout,
            `Unable to find element: ${elementName}`
        );
        return result;
    }

    async elementByXpath(xpath, timeout = 5000) {
        const selector = this.webdriver.By.xpath(xpath);
        const result = await this.wait(selector, xpath, timeout);
        return result;
    }

    // Click when the element is displayed and enable.
    async click(element, timeout = 5000) {
        await this.driver.wait(
            this.webdriver.until.elementIsVisible(element),
            timeout
        );
        await this.driver.wait(
            this.webdriver.until.elementIsEnabled(element),
            timeout
        );

        await this.driver.executeScript('arguments[0].click();', element);
    }

    async clickByXPath(xpath, timeout = 5000) {
        const element = await this.elementByXpath(xpath, timeout);
        await this.click(element, timeout);
    }

    async insert(element, argument, timeout = 5000) {
        await this.driver.wait(
            this.webdriver.until.elementIsVisible(element),
            timeout
        );
        await this.driver.wait(
            this.webdriver.until.elementIsEnabled(element),
            timeout
        );

        await element.sendKeys(argument);
    }

    async insertByXPath(xpath, argument, timeout = 5000) {
        const element = await this.elementByXpath(xpath);
        return this.insert(element, argument, timeout);
    }

    async getVal(element) {
        return await element.getAttribute("value");
    }

    async getValByXPath(xpath) {
        const element = await this.elementByXpath(xpath);
        return await this.getVal(element);
    }

    async clearInput(element) {
        await this.driver.executeScript(elt => elt.select(), element);
        await element.sendKeys(this.webdriver.Key.BACK_SPASE);
    }

    async clearInputByXPath(xpath) {
        const element = await this.elementByXpath(xpath);
        await this.clearInput(element);
    }

    // If the element isn't visible, create error.
    async elementIsVisible(element, timeout = 15000) {
        await this.driver.wait(
            this.webdriver.until.elementIsVisible(element),
            timeout
        );
    }

    async elementIsVisibleByXPath(xpath, timeout = 15000){
        const element = await this.elementByXpath(xpath);
        await this.elementIsVisible(element, timeout);
    }
  }
  
  
module.exports = BasePage;