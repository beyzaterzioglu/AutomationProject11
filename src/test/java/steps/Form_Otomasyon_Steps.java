package steps;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.thoughtworks.gauge.Step;
import driver.Driver;
import org.assertj.core.api.Assert;
import org.junit.jupiter.api.Assertions;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.pagefactory.ElementLocator;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.time.Duration;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.NoSuchElementException;

public class Form_Otomasyon_Steps {
    WebDriver driver = Driver.webDriver;
    WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));

    private static Map<String, Map<String, String>> elements;

    private WebElement find(String key) {
        return Driver.webDriver.findElement(getLocator(key));
    }

    static {
        try {
            ObjectMapper mapper = new ObjectMapper();
            InputStream elementStream = Form_Otomasyon_Steps.class.getClassLoader().getResourceAsStream("elements.json");

            List<Map<String, String>> elementList = mapper.readValue(
                    elementStream,
                    new TypeReference<List<Map<String, String>>>() {
                    }
            );

            elements = new HashMap<>();
            for (Map<String, String> element : elementList) {
                String key = element.get("key");
                elements.put(key, element);
            }

        } catch (Exception e) {
            throw new RuntimeException("JSON dosyaları okunamadı", e);
        }
    }

    private By getLocator(String key) {
        Map<String, String> locatorData = elements.get(key);
        String type = locatorData.get("type");
        String value = locatorData.get("value");

        return switch (type.toLowerCase()) {
            case "id" -> By.id(value);
            case "xpath" -> By.xpath(value);
            case "class" -> By.className(value);
            case "css" -> By.cssSelector(value);
            default -> throw new IllegalArgumentException("Desteklenmeyen locator türü: " + type);
        };
    }


    public String getJsonValue(String key) {
        ObjectMapper mapper = new ObjectMapper();
        try {
            Map<String, Object> jsonMap = mapper.readValue(new File("src/test/resources/values.json"), Map.class);
            Object value = jsonMap.get(key);
            return value != null ? value.toString() : null;
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }


    @Step("<url> adresini aç.")
    public void urlAc(String url) {
        String actualUrl = getJsonValue(url);
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver");
        Driver.start();
        if (actualUrl == null) {
            actualUrl = url;
        }
        Driver.webDriver.get(actualUrl);

        Assertions.assertEquals(actualUrl, Driver.webDriver.getCurrentUrl(),
                "Sayfa URL'si beklenenle uyuşmuyor.");
    }

    @Step("<alan> alanına <name> degerini yaz.")
    public void fieldDoldurma(String alan, String name) throws InterruptedException {

        String value = getJsonValue(name);
        if (value == null) {
            throw new RuntimeException("JSON'dan değer alınamadı: " + name);
        }
        WebElement element = find(alan);
        element.clear();
        element.sendKeys(value);
    }


    @Step("<key> alanına tıklanır")
    public void fieldClick(String key) throws InterruptedException {
        WebElement button = find(key);
        ((JavascriptExecutor) driver).executeScript("arguments[0].scrollIntoView(true);", button);
        button.click();
    }



    @Step("Kayıt işlemin onaylandığı <header> başlığına bakarak doğrulanır")
    public void headerDogrulama(String expectedHeader) {
        WebDriverWait wait = new WebDriverWait(Driver.webDriver, Duration.ofSeconds(20));

        String expected=find("header").getText();
        WebElement headerElement = wait.until(
                ExpectedConditions.visibilityOfElementLocated(By.id("example-modal-sizes-title-lg"))
        );

        String actualHeaderText = headerElement.getText();
        Assertions.assertEquals(expected, actualHeaderText,
                "Başlık beklenenle uyuşmuyor! Beklenen: " + expected + ", Gerçek: " + actualHeaderText);

        System.out.println("Başlık doğrulandı: " + actualHeaderText);
    }


    @Step("Kayıt işleminin onaylanmadığı doğrulanır")
    public void headerGorunmediginiDogrulama() {

        WebElement submitButton = find("SubmitButton");
        ((JavascriptExecutor) driver).executeScript("arguments[0].scrollIntoView(true);", submitButton);
        submitButton.click();

        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        try {
            WebElement modalHeader = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("example-modal-sizes-title-lg")));
            Assertions.fail("Başlık görünüyor, yani kayıt işlemi başarılı olmuş.");
        } catch (TimeoutException e) {
            System.out.println("Kayıt başarılı değil. Başlık bulunamadı. Test PASSED.");
        }

    }

    @Step("Dosya seçimi yapılır")
    public void dosyaSec() {

        WebElement uploadInput = find("UploadPicture");

        String dosyaYolu = getJsonValue("filePath");
        if (dosyaYolu == null || dosyaYolu.isEmpty()) {
            throw new RuntimeException("values.json dosyasından 'filepath' değeri alınamadı.");
        }
        uploadInput.sendKeys(dosyaYolu);
        String uploadedFileName = uploadInput.getAttribute("value");
        Assertions.assertFalse(uploadedFileName.isEmpty(), "Dosya seçimi yapılmadı!");
    }

    @Step("Gelecekte olan bir doğum tarihi seçilir")
    public void gelecekteOlanBırGunSec() {
        Select yearSelect = new Select(find("yearSelect"));
        yearSelect.selectByVisibleText(getJsonValue("year"));
    }


    @Step("<key> alanına tıklanır ardından boşluğa tıklanır")
    public void tıklamaSonrasıBoslugaTıkla(String key) {

        WebElement element = new WebDriverWait(driver, Duration.ofSeconds(10))
                .until(ExpectedConditions.visibilityOf(find(key)));

        new WebDriverWait(driver, Duration.ofSeconds(10))
                .until(ExpectedConditions.elementToBeClickable(element));
        element.click();
        WebElement body = driver.findElement(By.tagName("body"));
        body.click();
    }



}
