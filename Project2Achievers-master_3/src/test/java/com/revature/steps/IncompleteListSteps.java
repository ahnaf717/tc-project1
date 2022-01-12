package com.revature.steps;

import com.revature.runner.TestRunner;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;
import org.openqa.selenium.support.ui.ExpectedConditions;

public class IncompleteListSteps {

    @Given("The Customer is on the Customer Dashboard Page.")
    public void the_customer_is_on_the_customer_dashboard_page() {
        // Write code here that turns the phrase above into concrete actions
        TestRunner.driver.get("http://127.0.0.1:5500/Customer-Dashboard.html");
    }
    @When("The Customer clicks on the Incomplete Lists button.")
    public void the_customer_clicks_on_the_incomplete_lists_button() {
        TestRunner.explicitWait.until(ExpectedConditions.elementToBeClickable(TestRunner.incompleteLists.incompleteButton));
        TestRunner.incompleteLists.incompleteButton.click();
    }
    @Then("The Customer should be able to view his incomplete lists.")
    public void the_customer_should_be_able_to_view_his_incomplete_lists() {
        String title = TestRunner.driver.getTitle();
        Assert.assertEquals(title,title);
    }

}
