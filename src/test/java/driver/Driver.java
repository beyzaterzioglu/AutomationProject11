package driver;

import com.thoughtworks.gauge.AfterScenario;
import com.thoughtworks.gauge.BeforeScenario;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import io.github.bonigarcia.wdm.WebDriverManager;

public class Driver {
    public static WebDriver webDriver;

    @BeforeScenario
    public static void start() {
        if (webDriver == null) {
            WebDriverManager.chromedriver().setup();
            webDriver = new ChromeDriver();
        }
    }

    @AfterScenario
    public static void stop() throws InterruptedException {
        if (webDriver != null) {
            webDriver.quit();
            webDriver = null;
        }
    }
}
