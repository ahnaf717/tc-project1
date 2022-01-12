package com.revature.steps;

import com.revature.runner.TestRunner;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.testng.Assert;


public class ShopperLoginSteps {
    @Given("The shopper is on the login page")
    public void the_shopper_is_on_the_login_page() {
        TestRunner.driver.get("http://127.0.0.1:5500/Index.html");
    }
    @When("The shopper enters username into username input box")
    public void the_shopper_enters_username_into_username_input_box() {
        TestRunner.shopperLoginPage.inputUsername.sendKeys("mia");
    }
    @When("The shopper enters password into password input box")
    public void the_shopper_enters_password_into_password_input_box() {
        TestRunner.shopperLoginPage.inputPassword.sendKeys("mia");
    }
    @When("The shopper clicks the login button")
    public void the_shopper_clicks_the_login_button() {
        TestRunner.shopperLoginPage.loginButton.click();
    }
    @Then("The shopper is redirected to the Shopper Dashboard")
    public void the_shopper_is_redirected_to_the_shopper_dashboard() {
        TestRunner.explicitWait.until(ExpectedConditions.titleIs("Shopper Dashboard"));
        String shopperDash = TestRunner.driver.getTitle();
        Assert.assertEquals(shopperDash, "Shopper Dashboard");

    }

}
