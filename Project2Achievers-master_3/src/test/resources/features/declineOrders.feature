Feature:A Shopper should be able to decline a order.


  Scenario:As a shopper I want to decline a order if I can not deliver.
    Given The Shopper is on the Current Shopping List Page.
    When The Shopper clicks on the Decline Button.
    Then The Shopper should be redirected to the Shopper Dashboard Page.