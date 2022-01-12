package com.revature.runner;


import com.revature.poms.*;
import io.cucumber.junit.Cucumber;
import io.cucumber.junit.CucumberOptions;
import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.runner.RunWith;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.io.File;
import java.time.Duration;
import java.util.concurrent.TimeUnit;

    @RunWith(Cucumber.class)

    @CucumberOptions(features = "classpath:features", glue = "com/revature/steps")
    public class TestRunner {
        public static WebDriver driver;
        public static IncompleteLists incompleteLists ;
        public static CompletedLists completedLists;
        public static DeclineOrder declineOrder;
        public static OrderCompleted orderCompleted;
        public static LoginPage loginPage;
        public static ShopperLoginPage shopperLoginPage;
        public static ShopperRegisterPage shopperRegisterPage;
        public static CustomerRegister customerRegister;
        public static CustomerDashboardPage customerDashboardPage;
        public static WebDriverWait explicitWait;



        @BeforeClass
        public static void setup() {
            File file = new File("src/test/resources/chromedriver.exe");
            System.setProperty("webdriver.chrome.driver", file.getAbsolutePath());
            driver = new ChromeDriver();
            incompleteLists = new IncompleteLists(driver);
            completedLists= new CompletedLists(driver);
            declineOrder=new DeclineOrder(driver);
            orderCompleted=new OrderCompleted(driver);
            loginPage = new LoginPage(driver);
            shopperLoginPage = new ShopperLoginPage(driver);
            shopperRegisterPage = new ShopperRegisterPage(driver);
            customerDashboardPage = new CustomerDashboardPage(driver);
            customerRegister = new CustomerRegister(driver);

            System.out.println("setup complete!");
            driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(1));
            explicitWait = new WebDriverWait(driver, Duration.ofSeconds(3, 1));
        }


        @AfterClass
        public static void teardown() {
            driver.quit();
            System.out.println("teardown complete!");
        }


    }

