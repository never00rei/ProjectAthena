# Project Athena

**_What is Athena?_**

Athena is a Slack bot for operations, connecting to services providing metrics and then spitting them back out as graphs or just condensed statistics.

**_What can Athena currently do?_**

Currently Athena can greet you, responding to direct messages or just listening in for keywords or service names in channels.

**_What is planned for Athena?_**
+ Slack based management of services: creating links to services, updating links to services and amending user based permissions.
+ Conversational responses to queries about services Athena is linked to.

  For instance, if you were to say:

  > @Athena is google up?

  Athena would respond in kind based on the severity of the issue.


**_What services or checks are you planning on integrating with or creating?_**

There are a couple of services I'm currently planning on writing API calls for off the bat:
1. Datadog:

   All metrics associated with a service saved in Athena, either based on tags or hostname stored in datadog.
2. Google Apps, more importantly Google sheets:

   From Google sheets you will be able to pull out statistics from specific sheets and cells or multiple sheets and cells in response to indirect messages or direct messages.

Custom checks I'm looking to create:
1. Ping check
2. Web site or web page response time
3. Cron style service checks


I have got others that I have in mind but, for the moment, these are the only two that are planned.

## Current to do:

**__Responses__**
1. **~~Greetings~~**
2. **Context manager**
   1. Write a function for parsing text and pattern matching for contextual information like service name, checks and or dates.
3. **Statistics**
   1. ~~Mock line graph data points between two dates~~
   2. Write function for handling and presenting single data points
   3. Write function for handling and presenting multiple data points
   4. Write wrapper for presenting data in graph format

**_Service Integration_**
1. API Calls
   1. Datadog
   2. Google Apps

**_Database_**
1. Database connector
2. Create base database models:
   * User accounts
   * User permissions
   * Services
   * Service integrations
   * Service checks