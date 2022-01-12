package com.revature.steps;

import com.revature.runner.TestRunner;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;
import org.openqa.selenium.support.ui.ExpectedConditions;

public class DeclineOrderSteps {

    @Given("The Shopper is on the Current Shopping List Page.")
    public void the_shopper_is_on_the_current_shopping_list_page() {
        TestRunner.driver.get("http://127.0.0.1:5500/Shopper-on-the-list.html");
    }

    @When("The Shopper clicks on the Decline Button.")
    public void the_shopper_clicks_on_the_decline_button() {
        TestRunner.explicitWait.until(ExpectedConditions.elementToBeClickable(TestRunner.declineOrder.deleteButton));
        TestRunner.declineOrder.deleteButton.click();
        TestRunner.driver.switchTo().alert().accept();
    }
    @Then("The Shopper should be redirected to the Shopper Dashboard Page.")
    public void the_shopper_should_be_redirected_to_the_shopper_dashboard_page() {

        String title = "http://127.0.0.1:5500/Shopper-Dashboard.html";
        Assert.assertEquals(title,title);
    }


}
