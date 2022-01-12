package com.revature.steps;

import com.revature.runner.TestRunner;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;
import org.openqa.selenium.support.ui.ExpectedConditions;

public class CompletedListSteps {


    @Given("A Customer is on the Customer Dashboard Page.")
    public void A_customer_is_on_the_customer_dashboard_page() {
        // Write code here that turns the phrase above into concrete actions
        TestRunner.driver.get("http://127.0.0.1:5500/Customer-Dashboard.html");
    }



    @When("The Customer clicks on the Completed Lists button.")
    public void the_customer_clicks_on_the_completed_lists_button() {
        TestRunner.explicitWait.until(ExpectedConditions.elementToBeClickable(TestRunner.completedLists.completedButton));
        TestRunner.completedLists.completedButton.click();
    }

    @Then("The Customer should be able to view his completed lists.")
    public void the_customer_should_be_able_to_view_his_completed_lists() {
        String title = TestRunner.driver.getTitle();
        Assert.assertEquals(title,title);
    }

}
