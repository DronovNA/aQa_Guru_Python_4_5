from selene import browser, command
from selene import be, have
import os


def test_form(hold_browser):
    browser.open("https://demoqa.com/automation-practice-form")
    browser.element("#firstName").should(be.blank).type("Test")
    browser.element("#lastName").should(be.blank).type("Testovich")
    browser.element("#userEmail").should(be.blank).type("Test@example.com")
    browser.element('[for="gender-radio-2"]').should(be.clickable).click()
    browser.element("#userNumber").should(be.blank).type("89997589856")
    browser.execute_script("window.scrollBy(0, 500)")
    browser.element("#dateOfBirthInput").should(be.clickable).click()
    browser.element('[value="1998"]').should(be.clickable).click()
    browser.element('[class="react-datepicker__day react-datepicker__day--001 react-datepicker__day--weekend"]').should(
        be.clickable
    ).click()
    browser.element('.subjects-auto-complete__input>input').should(be.blank).type("sci").press_enter()
    browser.element('[for="hobbies-checkbox-2"]').should(be.clickable).perform(command.js.click)
    browser.element("#uploadPicture").send_keys(os.getcwd() + '\example.png')
    browser.element("#currentAddress").should(be.blank).type("Test test test")
    browser.element('footer').perform(command.js.remove)
    browser.element("#state").should(be.clickable).click()
    browser.element('//div[text()="NCR"]').should(be.clickable).click()
    browser.element("#city").should(be.clickable).click()
    browser.element('//div[text()="Delhi"]').should(be.clickable).click()
    browser.element("#submit").submit()
    browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))

    # check_result
    browser.all(".table-responsive td").by(
        have.exact_texts(
            "Test Testovich"
            "Test@example.com"
            "Female"
            "8999758985"
            "01 March,1998"
            "Computer Science"
            "Reading"
            "example.txt"
            "Test test test"
            "NCR Delhi"
        )
    )
