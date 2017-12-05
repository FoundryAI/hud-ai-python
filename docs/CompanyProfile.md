# CompanyProfile

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`          		| String     | Resource ID **Cannot be edited** |
| `company_id`* 		| **String** | Associated company |
| `description` 		| String     | High-level description of company |
| `profile_image_url`	| String 	 | Company logo url |
| `homepage_url`    	| String 	 | Company homepage |
| `linkedin_url`  		| String  	 | Company LinkedIn page|
| `city`    			| String  	 | The city in which the Company is Headquartered |
| `state`    			| String  	 | The state (full name eg. Californina) in which the Company is Headquartered |
| `Country`    		 	| String  	 | The country (full name) in which the Company is Headquartered |

## `client.company_profile.fetch(company_id)`

This is a read only endpoint
