package com.revature.poms;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;


public class IncompleteLists {

    private WebDriver driver;


    public IncompleteLists(WebDriver driver){
        this.driver = driver;
        // the PageFactory handles finding and assigning web elements to the properties we declared below
        PageFactory.initElements(driver,this);
    }

    @FindBy(id = "incompleted")
    public WebElement incompleteButton;


}
