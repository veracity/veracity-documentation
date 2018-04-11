---
Title: Notification service
Author: "Tong, Xiao Gang Tony"
Contributors: "Brede Børhaug"
---

## Introduction
A notification is a short message to a customer telling them that you have some new information that you think is relevant for him or her to know. The notification can have links to further information or an action you want the customer to do but it should not be a lengthy text.

Examples:
- We just updated your container with the latest result data.
- A new DNV GL service specification (SE) Qualification of manufacturers of special materials(DNVGL-SE-0079) has been published.

A notification is not an action/task but some notifications could be notifying you that an action might be needed.

A notification should not be used as general information newsletters or for marketing purposes. 

## How does it work? 

When your customers are using your digital service, they can also subcribe to notifications related to your digital service if the service is offering notifications.The customers can set their notification preferences. The preferences to set are:

- If they want to subscribe to notifications from a service or not 
- How they want the notification delivered


We are offering delivery of notifications on different user interfaces/devices:

- Receive notification through web (visible in Veracity and in the web pages of the digital service)
- Receive notification through email, currently with frequency options of immediately, daily or weekly
- Receive push notification to a native mobile app that is related to a Veracity service
- Receive notification as SMS (this will be available in the near future)

The digital services can then use this notification channel to reach either all customers who subscribe to the channel or specific customers who subscribe to the channel.

Based on the customers preferences on how they want the notification delivered, Veracity wil deliver the notification.

If a digital service is offering different kind of notifications, these can be set up as separate notification channels so that the customer can subscribe to them independently.

## How to send notification through Notification Service

Service API has provided the API methods to use the notification service, you can find the details [here](https://developer.veracity.com/doc/service-api).

## How to develop mobile apps to use push notification

Notification Service can support to send push notification to native mobile apps in all kinds of different devices like Android, iOS, Windows phone etc. To be able to use the push notification from Veracity, you need to do the two things below:

-  In your native app, register notification template in Veracity Service notification hub when the app starts, and implement the display of notification if the notification is received while the app is active.
- In your back-end application, which is supposed to send notification, it needs to call Notification API to send broadcast notification to all users of the app or notification to specified users.

### How to connect your app to Veracity notification hub

#### iOS development

1. If you have no experience with Notification Hub and iOS development, please read through this  [guide](https://docs.microsoft.com/en-us/azure/notification-hubs/notification-hubs-ios-apple-push-notification-apns-get-started) on how to develop an mobile app on iOS to register notification template and receive notification.

2. When register your app for push notifications:
  - If you are using explicit app id, then it means you need a separated notification hub for your app to send push notification. Please generate a certification for your app id through Apple Developer Center. After you get the certification, please send it to Veracity team. Veracity team will create a notification hub for your app, and configure the apple notification service to use the certificate to send push notification. 
  - If you are using wildcard app id, please check with Veracity team whether this app id has already been registered in Notification Service. If it is already registered, you can ask for the notification hub name and connection string for this wildcard app id. If it hasn't been registered yet, please generate a certification for your app id through Apple Developer Center. Then you can ask Veracity team to create notification hub and send you back the hub name and connection string.
  -  Now we have provided the below notification hub:

Hub name | App Id Suffix (bundle id) | Certificate File | Demo App
-------- | ------------------------- | ---------------- | ---------
mydnvglnotification | com.dnvgl.mydnvglnotificationdemo | MyDNVGLNotificationDemo.p12 | MyDNVGLNotificationDemo-Prod.ipa

3. Notification Service uses templates to send platform-agnostic notifications targeting all devices across platforms. For this reason you need to define your notification template that you would like to use for your app users, here's an example:

``` Object C: 
NSString* templateBodyAPNS = @"{\"aps\":{\"alert\":\"$(Message)\", \"action\":\"$(action)\", \"type\":\"$(type)\"}}";
```
when you send notification through Veracity Notification API, you can provide the value for those template parameters.  

4. For broadcast notification, you need to get the Channel Id from your service admin. Then you need to use the Channel Id ("channel:<GUID>") as tags when registering the template in the notification hub. Here's an example:
  
``` Object C:
NSMutableArray* catArray = [[NSMutableArray alloc] init];
for(NSString *category in categories.allObjects)
{
  NSMutableString *final = [[NSMutableString alloc] initWithString:@"channel:"];
  [final appendString:category];
  [catArray addObject: final];
}
NSSet *tags = [NSSet setWithArray:catArray];
result = [hub registerTemplateWithDeviceToken:self.deviceToken name:@"simpleAPNSTemplate" jsonBodyTemplate:templateBodyAPNS expiryTemplate:@"0" tags:tags error:&error];
```

5. For sending a notification to specified users, you need to register the user id after the user logs into your app. Then you can register the user id ("user:<GUID>") as an additional tag on Channel Id.
  
6. To show the notification when it's received whilst the app is active, you need to implement the method didReceiveRemoteNotification on AppDelegate.m as the demo application.

#### Android development

1. If you are not familiar with Notification Hub and Android development, please read through this [guide](https://docs.microsoft.com/en-us/azure/notification-hubs/notification-hubs-chrome-push-notifications-get-started) on how to develop an mobile app on Android to register notification template and receive notification.

2. When register your app for push notifications:
Please check with MYDNVGL team and ask for th notification hub name,sender id and connection string.
Now we have provided below notification hub:

Hub name | SenderID | DemoApp
-------- | -------- | -------
MyDNVGLNotification | 570154396303 | AndroidDemoProd

3. Notification Service uses templates to send platform-agnostic notifications targeting all devices across platforms and we can push notifications by using tags. On android side you should define template to accept the message:

```
 String templateBodyGCM = "{\"data\":{\"message\":\"$(message)\",\"open_type\":\"$(open_type)\"}}";  
 ```
 when you send notification through Veracity Notification API, you can provide the value for those template parameters. 
 
 4. For broadcast notification, you need to get the Channel Id which you need to ask from your service admin. Veracity can register this channel id ("channel:<GUID>") as a basic tag for receiving broadcast notifications
 
 5. For sending a notification to specified users, you need to register the user id after the user logs into your app. Then you can register the user id ("user:<GUID>") as an additional tag on Channel Id.  
 
 ``` 
public void subscribeToCategories(final Set<String> categories) {
  new AsyncTask<Object, Object, Object>() {
  @Override
  protected Object doInBackground(Object... params) {
  try {
  if(!categories.contains(NotificationSettings.BasicChannelID)){
  categories.add(NotificationSettings.BasicChannelID);
  }
  String regid = gcm.register(senderId);
  String templateBodyGCM = "{\"data\":{\"message\":\"$(message)\",\"open_type\":\"$(open_type)\"}}";
  hub.registerTemplate(regid,"simpleGCMTemplate", templateBodyGCM,
  categories.toArray(new String[categories.size()]));
  } catch (Exception e) {
  Log.e("MainActivity", "Failed to register - " + e.getMessage());
  return e;
  }
  return null;
  }
  protected void onPostExecute(Object result) {
  String message = "Subscribed for categories: "+ categories.toString();
  Toast.makeText(context, message,
  Toast.LENGTH_LONG).show();
  cts = categories;
  }
  }.execute(null, null, null);
}
```           

6. How to show the notification when it's received while the app is active, you need to implement the method onReceive on MyHandler.java as the demo application.

### How to send notification through your back-end application
It needs to call Send Message API to send notification, please refer [Service API](https://developer.veracity.com/doc/service-api) for Notification. 
