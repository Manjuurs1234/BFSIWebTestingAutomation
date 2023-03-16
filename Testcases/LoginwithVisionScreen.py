import psycopg2 as pg
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from PageObjes.dyno_pom import Loginpage
class TestLogin:

    def test_Login(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        serv_obj = Service("Loginpage.chrome")
        self.driver = webdriver.Chrome(options=options, service=serv_obj)
        self.driver.maximize_window()
        self.driver.get(Loginpage.URL)
        time.sleep(2)
        self.driver.find_element(By.XPATH, Loginpage.textbox_mailid_xpath).send_keys(Loginpage.email)
        time.sleep(5)
        shadow = self.driver.find_element(By.CSS_SELECTOR, Loginpage.next)
        shadow.click()
        time.sleep(5)

        port = '5432'
        host = '34.100.216.73'
        user = "postgres"
        password = "t3djo7b0jfd9J3JL"
        database = "devdyno"

        con = pg.connect(database=database, user=user, password=password, host=host, port=port)
        cur = con.cursor()
        QueryString = '''SELECT (payload ->>'OTP') :: integer FROM auth.nq Order by pid desc limit 1'''
        cur.execute(QueryString)
        con.commit()
        output1 = cur.fetchall()
        a = str(output1)
        b = a.replace('[(', '')
        otp = b.replace(',)]', '')
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter OTP']").send_keys(otp)
        time.sleep(5)
        shadow1 = self.driver.find_element(By.CSS_SELECTOR,".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated")
        shadow1.click()
        time.sleep(5)

        # list view click
        self.driver.find_element(By.CSS_SELECTOR,"body > app-root:nth-child(1) > ion-app:nth-child(1) > ion-router-outlet:nth-child(1) > app-home:nth-child(2) > ion-content:nth-child(3) > div:nth-child(1) > ion-toolbar:nth-child(1) > ion-grid:nth-child(1) > ion-row:nth-child(1) > ion-col:nth-child(4) > div:nth-child(1) > ion-item:nth-child(2) > img:nth-child(1)").click()
        # search project card
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search Apps']").send_keys('BFSI')  # search name
        self.driver.find_element(By.CSS_SELECTOR,"body > app-root:nth-child(1) > ion-app:nth-child(1) > ion-router-outlet:nth-child(1) > app-home:nth-child(2) > ion-content:nth-child(3) > div:nth-child(1) > div:nth-child(3) > ion-card:nth-child(1) > ion-item:nth-child(1) > img:nth-child(3)").click()  # 3 dots
        # view specifications
        self.driver.find_element(By.ID, "logout-id").click()
         #******************************************************************************************************************
        # Screen Name: Vision Screen
        # SID: 2.1 - Verify UI elements of Vision Screen

        # User clicks on Vision link in left pane
        self.driver.find_element(By.CSS_SELECTOR, "body > app-root:nth-child(1) > ion-app:nth-child(1) > ion-router-outlet:nth-child(1) > app-landing:nth-child(3) > ion-content:nth-child(3) > ion-grid:nth-child(1) > ion-row:nth-child(1) > ion-col:nth-child(2) > div:nth-child(2) > ion-grid:nth-child(1) > ion-row:nth-child(1) > ion-col:nth-child(1) > app-multi-level-menu:nth-child(1) > ion-content:nth-child(1) > div:nth-child(1) > div:nth-child(1) > li:nth-child(1) > ion-row:nth-child(1) > ion-col:nth-child(3) > ion-row:nth-child(1)").click()
       # Displaying user navigation in top menu and Title indicating the vision number
        self.driver.find_element(By.CSS_SELECTOR, ".bread-crumb-col.md.hydrated")
        # # see the Document status drop down
        self.driver.find_element(By.CSS_SELECTOR, "img[src='../../../../assets/icon/pencil.png']").click() # click the edit button
        self.driver.find_element(By.XPATH, '//*[@id="mat-select-0"]/div/div[2]').click()  # click the dropdown
        self.driver.find_element(By.CSS_SELECTOR, "mat-option[id='mat-option-4'] span[class='mat-option-text']").click()  # click the draft
        # click button
        self.driver.find_element(By.CSS_SELECTOR, "ion-col[class='ion-align-self-center items-col md hydrated'] ion-col:nth-child(2)").click()
        # Comments icon
        self.driver.find_element(By.CSS_SELECTOR, "img[src='../../../../assets/icon/comment_blue.png']")
        time.sleep(2)
        # Edit icon
        self.driver.find_element(By.CSS_SELECTOR, "img[src='../../../../assets/icon/pencil.png']")
        # see the more options
        self.driver.find_element(By.CSS_SELECTOR, ".ellipseMargin").click()
        # dark background
        self.driver.find_element(By.XPATH, "//div[@class='cdk-overlay-backdrop cdk-overlay-dark-backdrop cdk-overlay-backdrop-showing']").click()
        # see the textbox to enter the Title and Description
        self.driver.find_element(By.CLASS_NAME,"visionTitle")
        # Footer menu information
        self.driver.find_element(By.XPATH, "//div[@class='footerClass']")
       #  #*******************************************************************************************************
    #
    #     # SID 2.2 - Edit Vision Details
    #     # Edit icon
    #     self.driver.find_element(By.CSS_SELECTOR, "img[src='../../../../assets/icon/pencil.png']").click()
    #     time.sleep(2)
    #     # see the textbox to enter the modification Title and Description
    #     self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Please enter a title here']").clear()
    #     time.sleep(1)
    #     self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Please enter a title here']").send_keys("+VSN NO509")
    #     time.sleep(3)
    #     self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Please enter a title here']").clear()
    #     time.sleep(10)
    # #*****************************************************************************************************************
    #     # SID 2.3 - Save Vision Details
    #     # click save button
    #     self.driver.find_element(By.CSS_SELECTOR, "ion-col[class='ion-align-self-center items-col md hydrated'] ion-col:nth-child(1) ion-row:nth-child(1)").click()
    #     time.sleep(5)
    #
    #     # error message has not shown - bug nas raised. after solve the bug save, cancel and Delete SID's has work.
    #
    #     # User should be able to see More Options
    #     self.driver.find_element(By.XPATH, "//div[@class='footerClass']")
    #     time.sleep(2)
    # #***************************************************************************************************************
    #     # # SID 2.4 - Cancel saving details
    #     # self.driver.find_element(By.XPATH, "img[src='assets/icon/cancel-blue.png']").click()
    #     # time.sleep(2)
    #     # self.driver.find_element(By.XPATH, "//div[@class='footerClass']")
    #     # time.sleep(2)
    # #***************************************************************************************************************
    #     # # SID 2.5 - Delete vision details
    #     # self.driver.find_element(By.CSS_SELECTOR, "img[src='../../../../assets/icon/delete.png']").click()
    #     # time.sleep(2)
    #     # # Cancel the delete option
    #     # self.driver.find_element(By.XPATH, "//span[normalize-space()='Cancel']").click()
    #     # time.sleep(2)
    # #****************************************************************************************************************
    # #     # SID 2.6 - More options
    # #     # see the more options
    # #     self.driver.find_element(By.CSS_SELECTOR, ".ellipseMargin").click()
    # #     time.sleep(3)
    # #     # dark background
    # #     self.driver.find_element(By.XPATH,"//div[@class='cdk-overlay-backdrop cdk-overlay-dark-backdrop cdk-overlay-backdrop-showing']").click()
    # #     time.sleep(3)
    # #     # User should be able to see More Options
    # #     self.driver.find_element(By.XPATH, "//div[@class='footerClass']")
    # #     time.sleep(2)
    # #     # Click the more options again
    # #     self.driver.find_element(By.CSS_SELECTOR, ".ellipseMargin").click()
    # #     time.sleep(3)
    # # #******************************************************************************************************************
    #   # SID 2.7 - Upload Documents (should be allowed are .doc, .docx, .pdf, .jpeg, .png, .xls)
    #     #dark background
    #     self.driver.find_element(By.XPATH,"//div[@class='cdk-overlay-backdrop cdk-overlay-dark-backdrop cdk-overlay-backdrop-showing']").click()
    #     time.sleep(3)
    #     # Edit icon
    #     self.driver.find_element(By.CSS_SELECTOR, "img[src='../../../../assets/icon/pencil.png']").click()
    #     time.sleep(2)
    #     # Click the more options again
    #     self.driver.find_element(By.CSS_SELECTOR, ".ellipseMargin").click()
    #     time.sleep(3)
    #     # User should be able to upload a document from the local device
    #     self.driver.find_element(By.CSS_SELECTOR, "div[class='cdk-overlay-container'] ion-col:nth-child(1) ion-row:nth-child(1)").click()
    #     time.sleep(2)
    #    # User should see the warning message
    #     self.driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
    #     time.sleep(2)
    #       # document title
    #     self.driver.find_element(By.CSS_SELECTOR, "input[name='ion-input-1']").send_keys("demo img")
    #     time.sleep(2)
    #     # User should be able to see the uploaded documents in the vault section
    #     upload =  self.driver.find_element(By.XPATH, "//img[@class='uploadImg']").click()
    #     print("Element is Found : verified", upload.is_displayed())
    #     if upload.is_displayed() == True:
    #         assert True
    #     else:
    #         print("Element Not Found : Not verified", upload.is_displayed())
    #         img = "D:/BFSI Web Testing Automation/Images/testing2.jpg"
    #     self. driver.find_element(By.CSS_SELECTOR, ".uploadImg").send_keys(img)
    #     time.sleep(2)
    #     # Footer menu information
    #     self.driver.find_element(By.XPATH, "//div[@class='footerClass']")
    #     time.sleep(2)
    # # #*****************************************************************************************************************
    #     # SID 2.8 - View documents in Vault
    #     # see the more options
    #     self.driver.find_element(By.CSS_SELECTOR, ".ellipseMargin").click()
    #     time.sleep(3)
    #     # User should see be able to see a Upload Documents
    #     self.driver.find_element(By.CSS_SELECTOR, ".visionOptionsImg.padding-leftImg").click()
    #     time.sleep(5)
    #     # User should be able to pin the popup window by clicking on the Pin
    #     self.driver.find_element(By.XPATH, "//img[@class='pin']").click()
    #     time.sleep(5)
    # #******************************************************************************************************************
    #     # SID 2.9 - View selected document
    #     #  User viewing documents in the Vault
    #     self.driver.find_element(By.CSS_SELECTOR, ".ViewDocPopover.white-bg.pin-div").click()
    #     time.sleep(5)
    #    # User should be able to see the option to go back by clicking close button
    #     self.driver.find_element(By.CSS_SELECTOR, ".close_popover_icon.ng-star-inserted.md.hydrated").click()
    #     time.sleep(2)
    #     # User should be able to Pin the document by clicking on Pin icon
    #     self.driver.find_element(By.XPATH, "//img[@class='pin']").click()
    #     time.sleep(2)
    # #******************************************************************************************************************
    #     # SID 2.10 - View all people who are tagged to the vision
    #     # User is in the Vision Screen
    #     self.driver.find_element(By.CSS_SELECTOR, ".ellipseMargin").click()
    #     time.sleep(3)
    #     # User clicks on People Icon
    #     self.driver.find_element(By.CSS_SELECTOR, "img[src='../../../../assets/icon/view_person.png']").click()
    #     time.sleep(2)
    #     # User should be able to see a popup with all people to view
    #     self.driver.find_element(By.CSS_SELECTOR, ".addPeoplePopover.white-bg").click()
    #     time.sleep(2)
    #     # User should be able to Pin the document by clicking on Pin icon
    #     self.driver.find_element(By.XPATH, "//img[@class='pin']").click()
    #     time.sleep(2)
    #  #******************************************************************************************************************
    #     # SID 2.11 - View all tags associated with the vision
    #     # User is in the Vision Screen
    #     self.driver.find_element(By.CSS_SELECTOR, ".ellipseMargin").click()
    #     time.sleep(3)
    #     # User clicks on Tag Icon
    #     self.driver.find_element(By.CSS_SELECTOR, "img[src='../../../../assets/icon/view_tags.png']").click()
    #     time.sleep(2)
    #     # # User should be able to see a popup with all tags to view
    #     # self.driver.find_element(By.CSS_SELECTOR, "mat-chip[role='option']")
    #     # time.sleep(2)
    #     # User should be able to Pin the document by clicking on Pin icon
    #     self.driver.find_element(By.XPATH, "//img[@class='pin']").click()
    #     time.sleep(2)
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #      # validations
    #     Dashboard_display = self.driver.find_element(By.CSS_SELECTOR, ".visionTitle")
    #     print("Element Found : Focus On", Dashboard_display.is_displayed())
    #     print("Vision link options was verified:")
    #     print("User navigation in top menu and Title indicating the vision number was verified:")
    #     print("Document status drop down was verified:")
    #     print("Comments icon was verified:")
    #     print("Edit icon was verified:")
    #     print("More options button was verified:")
    #     print("The Title and Description was verified:")
    #     print("Footer menu information was verified:")
    #     print("Edit Vision Details was verified:")
    #     print("User should be able to see More Options was verified:")
    #     print("Save Vision Details was verified:")
    #     print("Cancel saving Details was verified:")
    #     print("Delete Vision  Details was verified:")
    #     print("More options button was again verified:")
    #     print("Upload Documents page was verified:")
    #     print("View documents in Vault message was verified:")
    #     print("View selected documents was verified:")
    #     print("View all people who are tagged to the vision was verified:")
    #     print("View all tags associated with the vision was verified:")
    #
    #     time.sleep(2)
    #     if Dashboard_display.is_displayed() == True:
    #         assert True
    #     else:
    #         print("Element Not Found : Not verified", Dashboard_display.is_displayed())
    #
    #     #self.driver.close()