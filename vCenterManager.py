import httplib2
import http.client, http.cookiejar
import urllib, os, time
import urllib.parse, urllib.request

class WebServletCtrol:
	def __init__(self):

		self.url = 'https://vcops/HttpPostAdapter/OpenAPIServlet'
		self.username = 'admin'
		self.password = 'admin'
		self.postdata = ''
		self.auth_realm = 'Alive Login'
		self.resourceName = 'Traffic'
		self.adapterKindKey = 'LBA'
		self.resourceKindKey = 'WORLD'
		self.identifiers = ''
		self.resourceDescription = ''
		self.monitoringInterval = ''
		self.storeOnly = ''
		self.sourceAdapter = ''
		self.metricsList = ''
		self.propertyList = ''
		self.disableResourceCreation = 'false'
		self.metricName = ''
		self.date = ''
		self.values = ''
		self.thresholdHigh = ''
		self.thresholdLow = ''
		self.propertyName = ''
		self.businessServiceNames = ''
		self.parentResource = ''
		self.childResources = ''
		self.addFlag = ''
		self.clearFirst = ''
		self.clearAdapterKinds = ''	
		self.eventTime = ''
		self.eventMessage = ''
		self.managedExternally = ''	
		self.criticalityLevel = ''	
		self.eventCancelTime = ''
		self.abnormalityTime = ''
		self.abnormalityCancelTime = ''
		self.abnormalityMessage = ''
		self.isKI = ''
		self.geoLocationName = ''
		self.latitude = ''
		self.longitude = ''
		self.resources = ''
		self.getParents = ''
		self.getChildren = ''
		self.metricKey = ''
		self.starttime = ''
		self.endtime = ''
		self.includeDt = ''
		self.includeSmooth = ''		
		self.metricKeys = ''
		
	def setUrl(self, rul):
		'''
		OpenAPIServlet Url
		'''
		self.url = url		
		
	def setUserName(self, username):
		'''
		Webpage login username
		'''
		self.username = username

	def setPasswd(self, password):
		'''
		Webpage login username
		'''
		self.password = password

	def _setPostdata(self, postdata):
		'''
		post function
		'''
		self.postdata = postdata		
		
	def setAuthRealm(self, auth_realm):
		'''
		Webpage login Realm
		'''
		self.auth_realm = auth_realm

	def setResName(self, resourceName):
		'''
		resourceName must not contain commas or spaces (required)
		'''
		self.resourceName = resourceName
	
	def setAdapterKindKey(self, adapterKindKey):
		'''
		adapterKindKey must not contain commas or spaces (required)
		'''
		self.adapterKindKey = adapterKindKey

	def setResKindKey(self, resourceKindKey):
		'''
		resourceKindKey must not contain commas or spaces (required)
		[Undefined|VirtualMachine|HostSystem|ResourcePool|ClusterComputeResource|Datacenter|Folder|ComputeResource
		|HostFolder|VmFolder|DatacenterFolder|VirtualApp|Datastore|DatastoreFolder|NetworkFolder|non-VC-DS_VM_RELSHP
		|VirtualCenter|World|GroupType|Group|VCMAdapter Instance|VinAdapter Instance|Container]
		'''
		self.resourceKindKey = resourceKindKey

	def setIdentifiers(self, identifiers):
		'''
		identifiers format should be identifier1_def$$identifier2_def$$...$$identifierN_def, 
		where identifierX_def=identifierKey::identifierValue[::isPartOfUniqueness]
		'''
		self.identifiers = identifiers
	
	def addMetricData(self, metricName,alarmLevel,alarmMessage,date,value,thresholdHigh = '',thresholdLow = ''):
		'''
		metricName must not contain commas (required)
		
		sourceAdapter specifies the adapter that the data comes from (optional). 
		If not specified, the generic "Http Post" adapter will be used.

		alarmLevel MUST be specified and is a number from 0 to 4 (required)
		
		alarmMesssage must not contain commas (required)
		
		date format:[2012/07/30 10:00:00] (required)
		
		values are integers or doubles (required)
		
		thresholdHigh and thresholdLow are doubles (optional)
		
		disableResourceCreation If it is true, resource will not be created, 
		otherwise if it is not specified or false resource will be created
		'''
		
		self.metricsList += (u'\r\n%s' % metricName)
		self.metricsList += (u',%s' % alarmLevel)
		self.metricsList += (u',%s' % alarmMessage)
		self.metricsList += (u',%s' % int((time.mktime(time.strptime(date, '%Y/%m/%d %H:%M:%S')))*1000))
		self.metricsList += (u',%s' % value)
		self.metricsList += (u',%s' % thresholdHigh)
		self.metricsList += (u',%s' % thresholdLow)
		
	def _cleanMetricsList(self):
		self.metricsList = ''
	
	def addProperty(self, propertyName, date, value):
		'''
		
		'''
		self.propertyList += (u'\r\n%s' % propertyName)
		self.propertyList += (u',%s' % int((time.mktime(time.strptime(date, '%Y/%m/%d %H:%M:%S')))*1000))
		self.propertyList += (u',%s' % value)

	def _cleanPropertyList(self):
		self.propertyList = ''		
		
	def setResDescription(self, resourceDescription):
		'''
		resourceDescription must not contain commas or spaces (optional)
		'''
		self.resourceDescription = resourceDescription

	def setMonitoringInt(self, monitoringInterval):
		'''
		monitoringInterval (in minutes) is how often 
		vCenter Operations Manager should expect data from this resource (optional; defaults to 5)
		'''
		self.monitoringInterval = monitoringInterval

	def setStoreOnly(self, storeOnly):
		'''
		storeOnly is whether the current data set should go through analytics processing 
		or not (valid values: 'true', 'on' or 'yes' (case insensitive) will set storeOnly 
		to true and disables analytics processing; false otherwise)  (optional; defaults to false)
		'''
		self.storeOnly = storeOnly

	def setSourceAdapter(self, sourceAdapter):
		'''
		sourceAdapter specifies the adapter that the data comes from (optional).
		If not specified, the generic "Http Post" adapter will be used.
		'''
		self.sourceAdapter = sourceAdapter
			
	def setDisableResCreation(self, disableResourceCreation):
		'''
		disableResourceCreation If it is true, resource will not be created, 
		otherwise if it is not specified or false resource will be created
		'''
		self.disableResourceCreation = disableResourceCreation

	def setMetricName(self, metricName):
		'''
		metricName must not contain commas (required)
		'''
		self.metricName = metricName
		
	def setValues(self, values):
		'''
		values are integers or doubles (required)
		'''
		self.values = values	
		
	def setBizSerNames(self, businessServiceNames):
		'''
		[comma-separated list of business service names]
		'''
		self.businessServiceNames = businessServiceNames
		
	def setParentResource(self, parentResource):
		'''
		[name_of_parent_resource]
		'''
		self.parentResource = parentResource
		
	def setChildResources(self, childResources):
		'''
		“;” separated list of child resources, 
		where each child resource must have comma separated resource name, 
		adapter kind key, resource kind key, identifiers
		'''
		self.childResources = childResources
	
	def setAddFlag(self, addFlag):
		'''
		true to add|false to remove
		'''
		self.addFlag = addFlag	
	
	def setClearFirst(self, clearFirst):
		'''
		true|false
		'''
		self.clearFirst = clearFirst
		
	def setClearAdapterKinds(self, setClearAdapterKinds):
		'''
		adapterKind1,adapterKind2,...,adapterKindN
		'''
		self.clearAdapterKinds = setClearAdapterKinds

	def setEventNoticeTime(self, eventTime):
		'''
		Epoch time notification appeared
		format:[2012/07/30 10:00:00]
		'''
		self.eventTime = int(time.mktime(time.strptime(eventTime, '%Y/%m/%d %H:%M:%S')))*1000
	
	def setEventCancelTime(self, eventCancelTime):
		'''
		Epoch time notification appeared
		format:[2012/07/30 10:00:00]
		'''
		self.eventCancelTime = int(time.mktime(time.strptime(eventCancelTime, '%Y/%m/%d %H:%M:%S')))*1000 

		
	def setEventMessage(self, eventMessage):
		'''
		descriptive message about notification
		'''
		self.eventMessage = eventMessage	
			
	def setManagedExternally(self, managedExternally):
		'''
		[true|false]
		'''
		self.managedExternally = managedExternally	
		
	def setCriticalityLevel(self, criticalityLevel):
		'''
		[none|info|warning|immediate|critical] 
		'''
		self.criticalityLevel = criticalityLevel			
		
	def setAbnormalityTime(self,abnormalityTime):
		'''
		[Epoch time abnormality appeared]
		format:[2012/07/30 10:00:00]
		'''
		self.abnormalityTime = int(time.mktime(time.strptime(abnormalityTime, '%Y/%m/%d %H:%M:%S')))*1000
	
	def setAbnormalityCancelTime(self,abnormalityCancelTime):
		'''
		[Epoch time abnormality Cancel]
		format:[2012/07/30 10:00:00]
		'''
		self.abnormalityCancelTime = int(time.mktime(time.strptime(abnormalityCancelTime, '%Y/%m/%d %H:%M:%S')))*1000
	
	def setAbnormalityMessage(self,abnormalityMessage):
		'''
		[descriptive message about abnormality]
		'''
		self.abnormalityMessage = abnormalityMessage
		
	def setIsKI(self,isKI):
		'''
		[true|false]
		'''
		self.isKI = isKI
	
	def setGeoLocationName(self,geoLocationName):
		'''
		[the name of GEO location]
		'''
		self.geoLocationName = geoLocationName
		
	def setLatitude(self,latitude):
		'''
		[latitude]
		'''
		self.latitude = latitude
	
	def setLongitude(self,longitude):
		'''
		[longitude]
		'''
		self.longitude = longitude
	
	def setResources(self, resources):
		'''
		[resourceName1,adapterKindKey1,resourceKindKey1,identifiers1;
		resourceName2,adapterKindKey2,resourceKindKey2,identifiers2;
		resourceNameN,adapterKindKeyN,resourceKindKeyN,identifiersN]
		'''
		self.resources = resources
		
	def setGetParents(self, getParents):
		'''
		[true|false]
		'''
		self.getParents = getParents
		
	def setGetChildren(self, getChildren):
		'''
		[true|false]
		'''
		self.getChildren = getChildren	
		
	def setMetricKey(self, metricKey):
		'''
		must not contain commas or spaces (required)
		'''
		self.metricKey = metricKey
		
	def	setStarttime(self,starttime):
		'''
		(required)
		format:[2012/07/30 10:00:00]	
		'''
		self.starttime = int(time.mktime(time.strptime(starttime, '%Y/%m/%d %H:%M:%S')))*1000
	
	def	setEndtime (self,endtime):
		'''
		(optional, defaults to current time)
		format:[2012/07/30 10:00:00]	
		'''
		self.endtime  = int(time.mktime(time.strptime(endtime , '%Y/%m/%d %H:%M:%S')))*1000
	
	def setIncludeDt(self,includeDt):
		''' 
		[true|false] 
		includes dynamic threshold values if available (optional, defaults to true)
		'''
		self.includeDt = includeDt
		
	def setIncludeSmooth(self,includeSmooth):
		'''
		[true|false] 
		includes smoothed data/moving average (optional, defaults to true)
		'''
		self.includeSmooth = includeSmooth		
		
	def setMetricKeys(self,metricKeys):
		'''
		metricKeys=[metrickey1], [metricKey2]...
		'''
		self.metricKeys = metricKeys
		
	def addGeneralMetricObservations(self):
		'''
		This interface is used to import metric data into vCenter Operations Manager, one resource at a time. 
		This interface handles the creation of the resource and resource kind, as well as any new metric names. 
		This is the default interface used when no "action" parameter is specified in the first line of body of the HTTP Post. 
		'''
		
		postdata = (u'%s'  % self.resourceName)
		postdata += (u',%s'% self.adapterKindKey)
		postdata += (u',%s'% self.resourceKindKey)
		postdata += (u',%s'% self.identifiers)
		postdata += (u',%s'% self.resourceDescription)
		postdata += (u',%s'% self.monitoringInterval)
		# postdata += (',%s'% self.storeOnly)
		# postdata += (',%s'% self.sourceAdapter)	
		# postdata += (',%s'% self.disableResourceCreation)
		
		#new line
		postdata += (u'%s' % self.metricsList)
		# print (postdata)
		self._cleanMetricsList();
		self._setPostdata(postdata)
		return c._postData()
	
	
	def addPropertyData(self):
		'''
		This interface is used to import property data into vCenter Operations Manager, one resource at a time. 
		This interface handles the creation of the resource and resource kind, as well as any new property names. 
		'''
		
		postdata = (u'action=addPropertyData')
		postdata += (u'&%s'% self.resourceName)
		postdata += (u',%s'% self.adapterKindKey)
		postdata += (u',%s'% self.resourceKindKey)
		postdata += (u',%s'% self.identifiers)
		postdata += (u',%s'% self.resourceDescription)
		postdata += (u',%s'% self.monitoringInterval)
		postdata += (u',%s'% self.sourceAdapter)
		postdata += (u',%s'% self.disableResourceCreation)
		
		#new line
		postdata += (u'%s'% self.propertyList)
		
		self._cleanPropertyList();
		self._setPostdata(postdata)
		return c._postData()
		
	def openResource(self):
		'''
		Use this interface to tell vCenter Operations Manager to accept data when it is pushed through the OpenAPI. 

		Optional sourceAdapter parameter specifies the adapter that is going to send data for the resource. 
		If sourceAdapter is not specified "Http Post" adapter is used. 
		'''
		
		postdata = (u'action=openResource')
		if (self.sourceAdapter) 	: postdata += (u'&sourceAdapter=%s'% self.sourceAdapter)
		if (self.resourceName)  	: postdata += (u'&resourceName=%s'% self.resourceName)
		if (self.adapterKindKey)	: postdata += (u'&adapterKindKey=%s'% self.adapterKindKey)
		if (self.resourceKindKey)	: postdata += (u'&resourceKindKey=%s'% self.resourceKindKey)
		if (self.identifiers)		: postdata += (u'&identifiers=%s'% self.identifiers)
		if (self.monitoringInterval): postdata += (u'&monitoringInterval=%s'% self.monitoringInterval)
		if (self.disableResourceCreation): postdata += (u'&disableResourceCreation=%s'% self.disableResourceCreation)
		
		self._setPostdata(postdata)
		return c._postData()		

	def stopResource(self):
		'''
		This function tells vCenter Operations Manager to stop accepting data for a particular resource. 

		Optional sourceAdapter parameter specifies the adapter that is going to stop sending data for the resource. 
		If sourceAdapter is not specified "Http Post" adapter is used. 		
		'''
		
		postdata = (u'action=stopResource')
		if (self.sourceAdapter)		: postdata += (u'&sourceAdapter=%s'% self.sourceAdapter)
		if (self.resourceName) 		: postdata += (u'&resourceName=%s'% self.resourceName)
		if (self.adapterKindKey)	: postdata += (u'&adapterKindKey=%s'% self.adapterKindKey)
		if (self.resourceKindKey)	: postdata += (u'&resourceKindKey=%s'% self.resourceKindKey)
		if (self.identifiers)		: postdata += (u'&identifiers=%s'% self.identifiers)
		
		self._setPostdata(postdata)
		return c._postData()		
		
	def removeResourceFromAdapterInstance(self):
		'''
		This function tells vCenter Operations Manager to remove a particular resource from adapter instance. 

		Optional sourceAdapter parameter specifies the adapter that is going to stop sending data for the resource. 
		If sourceAdapter is not specified "Http Post" adapter is used. 
		'''
		
		postdata = (u'action=removeResourceFromAdapterInstance')
		if (self.sourceAdapter)		: postdata += (u'&sourceAdapter=%s'% self.sourceAdapter)
		if (self.resourceName) 		: postdata += (u'&resourceName=%s'% self.resourceName)
		if (self.adapterKindKey)	: postdata += (u'&adapterKindKey=%s'% self.adapterKindKey)
		if (self.resourceKindKey)	: postdata += (u'&resourceKindKey=%s'% self.resourceKindKey)
		if (self.identifiers)		: postdata += (u'&identifiers=%s'% self.identifiers)
		
		self._setPostdata(postdata)
		return c._postData()			
		
	def getMonitoringResources(self):
		'''
		This function retrieves monitoring resources of associated with specified source adapter. 

		Optional sourceAdapter parameter specifies the adapter that is going to send monitoring resource for the resource. 
		If sourceAdapter is not specified "Http Post" adapter is used. 
		'''
		
		postdata = (u'action=getMonitoringResources')
		if (self.sourceAdapter) : postdata += (u'&sourceAdapter=%s'% self.sourceAdapter)

		self._setPostdata(postdata)
		return c._postData()	
	
	def getStoppedResources(self):
		'''
		This function retrieves stopped resources of associated with specified source adapter. 

		Optional sourceAdapter parameter specifies the adapter that is going to send stopped resource for the resource. 
		If sourceAdapter is not specified "Http Post" adapter is used. 
		'''
		
		postdata = (u'action=getStoppedResources')
		if (self.sourceAdapter) : postdata += (u'&sourceAdapter=%s'% self.sourceAdapter)

		self._setPostdata(postdata)
		return c._postData()			

	def configBusinessServiceFromXml(self):
		'''
		To do XML parse first
		'''	
		return 'None'
		
	def getBusinessServiceConfigAsXml(self):
		'''
		This function retrieves the configuration as XML for one or more business services. 
		'''
		
		postdata = (u'action=getBusinessServiceConfig')
		if (self.businessServiceNames) : postdata += (u'&businessServiceNames=%s' % self.businessServiceNames)

		self._setPostdata(postdata)
		return c._postData()	
	
	def addRemoveParentChildRelationship(self):
		'''
		Use this interface to Add or remove relationship entry in the ResourceMap table 
		and invoke analytics corresponding RMI method 

		Optional sourceAdapter parameter specifies the adapter that is managing relationships. 
		If sourceAdapter is not specified "Http Post" adapter is used. 

		Optional clearFirst parameter specifies if the existing children of specified parent resource 
		need to be removed before adding new children. If clearFirst is not specified it is "false" by default. 

		Optional clearAdapterKinds parameter specifies a comma delimited list of adapter kind keys for child resources 
		to be removed when clearing existing relationships. Only applies when clearFirst is true. 
		If specified only existing children of specified adapter kinds will be removed during clearFirst operation. 
		If not specified all children will be removed. 

		'''
		
		postdata = (u'action=addRemoveParentChildRelationship')
		if (self.sourceAdapter) 	: postdata += (u'&sourceAdapter=%s' % self.sourceAdapter)
		if (self.parentResource)	: postdata += (u'&parentResource=%s' % self.parentResource)
		if (self.adapterKindKey)	: postdata += (u'&adapterKindKey=%s' % self.adapterKindKey)
		if (self.resourceKindKey)	: postdata += (u'&resourceKindKey=%s' % self.resourceKindKey)
		if (self.identifiers)		: postdata += (u'&identifiers=%s' % self.identifiers)
		if (self.childResources)	: postdata += (u'&childResources=%s' % self.childResources)
		if (self.addFlag)			: postdata += (u'&addFlag=%s' % self.addFlag)
		if (self.clearFirst)		: postdata += (u'&clearFirst=%s' % self.clearFirst)
		if (self.clearAdapterKinds)	: postdata += (u'&clearAdapterKinds=%s' % self.clearAdapterKinds)
		
		self._setPostdata(postdata)
		return c._postData()		
	
	def addChangeEvent(self):
		'''
		Use this interface to push change events for a resource. 
		Change events are messages from external environments that would not generate alerts in vCenter Operations Manager 
		but can become a part of root cause analysis and appear in the vCenter Operations Manager UI. 

		Optional sourceAdapter parameter specifies the adapter that is sending the event. 
		If sourceAdapter is not specified "Http Post" adapter is used. 
		'''
		
		postdata = (u'action=addChangeEvent')
		if (self.sourceAdapter)		: postdata += (u'&sourceAdapter=%s' % self.sourceAdapter)
		if (self.resourceName)		: postdata += (u'&resourceName=%s' % self.resourceName)
		if (self.adapterKindKey)	: postdata += (u'&adapterKindKey=%s' % self.adapterKindKey)
		if (self.resourceKindKey)	: postdata += (u'&resourceKindKey=%s' % self.resourceKindKey)
		if (self.eventTime)			: postdata += (u'&time=%s' % self.eventTime)
		if (self.eventMessage)		: postdata += (u'&message=%s' % self.eventMessage)
		
		self._setPostdata(postdata)
		return c._postData()	
		
	def setResourceDown(self):
		'''
		Use this interface to set the resource status to "Resource down" and generate down alert for it. 
		As a result the Health of the resource will become 0. 
		
		Optional sourceAdapter parameter specifies the adapter that is sending the event. 
		If sourceAdapter is not specified "Http Post" adapter is used. 
		'''

		postdata = (u'action=setResourceDown')
		if (self.sourceAdapter)		: postdata += (u'&sourceAdapter=%s' % self.sourceAdapter)
		if (self.resourceName)		: postdata += (u'&resourceName=%s' % self.resourceName)
		if (self.adapterKindKey)	: postdata += (u'&adapterKindKey=%s' % self.adapterKindKey)
		if (self.resourceKindKey)	: postdata += (u'&resourceKindKey=%s' % self.resourceKindKey)
		if (self.identifiers)		: postdata += (u'&identifiers=%s' % self.identifiers)
		
		self._setPostdata(postdata)
		return c._postData()		
		
	def addNotificationEvent(self):
		'''
		Use this interface to push notification events for a resource. 
		Notification events are messages from external environments that can generate alerts in vCenter Operations Manager, 
		but are not a part of root cause analysis. 

		Optional sourceAdapter parameter specifies the adapter that is sending the event. 
		If sourceAdapter is not specified "Http Post" adapter is used. 

		Optional criticalityLevel parameter specifies the criticality level of the event. 
		If criticalityLevel is not specified "info" level is used. 

		'''
	
		postdata = (u'action=addNotificationEvent')
		if (self.sourceAdapter)		: postdata += (u'&sourceAdapter=%s' % self.sourceAdapter)
		if (self.resourceName)		: postdata += (u'&resourceName=%s' % self.resourceName)
		if (self.adapterKindKey)	: postdata += (u'&adapterKindKey=%s' % self.adapterKindKey)
		if (self.resourceKindKey)	: postdata += (u'&resourceKindKey=%s' % self.resourceKindKey)
		if (self.identifiers)		: postdata += (u'&identifiers=%s' % self.identifiers)
		if (self.eventTime)			: postdata += (u'&time=%s' % self.eventTime)
		if (self.eventMessage)		: postdata += (u'&message=%s' % self.eventMessage)		
		if (self.managedExternally)	: postdata += (u'&managedExternally=%s' % self.managedExternally)		
		if (self.criticalityLevel)	: postdata += (u'&criticalityLevel=%s' % self.criticalityLevel)		
		
		self._setPostdata(postdata)
		return c._postData()		
		
	def removeNotificationEvent(self):
		'''
		Use this interface to cancel notification events for a resource. 

		Optional sourceAdapter parameter specifies the adapter that is sending the event. 
		If sourceAdapter is not specified "Http Post" adapter is used. 
		'''
		
		postdata = (u'action=removeNotificationEvent')
		if (self.sourceAdapter)		: postdata += (u'&sourceAdapter=%s' % self.sourceAdapter)
		if (self.resourceName)		: postdata += (u'&resourceName=%s' % self.resourceName)
		if (self.adapterKindKey)	: postdata += (u'&adapterKindKey=%s' % self.adapterKindKey)
		if (self.resourceKindKey)	: postdata += (u'&resourceKindKey=%s' % self.resourceKindKey)
		if (self.identifiers)		: postdata += (u'&identifiers=%s' % self.identifiers)
		if (self.eventMessage)		: postdata += (u'&message=%s' % self.eventMessage)		
		if (self.eventCancelTime)	: postdata += (u'&cancelTime=%s' % self.eventCancelTime)			
		
		self._setPostdata(postdata)
		return c._postData()		
		
	def addHTAbove(self):
		'''
		Use this interface to push externally detected threshold violation event 
		for a particular metric of a particular resource (All fields are required) 
		Effects: 
			if resource does not exist, it is created with resourceKind and adapterKind given; 
			if the adapterKind does not exist, it is created; 
			if the resourceKind does not exist, it is created; 
			if the resourceKind does not contain an attribute with the name specified by metricName, 
			it is created 
		'''
		
		postdata = (u'action=addHTAbove')
		if (self.sourceAdapter) 	: postdata += (u'&sourceAdapter=%s' % self.sourceAdapter)
		if (self.resourceName)		: postdata += (u'&resourceName=%s' % self.resourceName)
		if (self.adapterKindKey)	: postdata += (u'&adapterKindKey=%s' % self.adapterKindKey)
		if (self.resourceKindKey)	: postdata += (u'&resourceKindKey=%s' % self.resourceKindKey)
		if (self.metricName)		: postdata += (u'&metricName=%s' % self.metricName)
		if (self.values)			: postdata += (u'&value=%s' % self.values)		
		if (self.abnormalityTime)	: postdata += (u'&time=%s' % self.abnormalityTime)
		if (self.abnormalityMessage): postdata += (u'&message=%s' % self.abnormalityMessage)			
		if (self.managedExternally)	: postdata += (u'&managedExternally=%s' % self.managedExternally)	
		if (self.isKI)				: postdata += (u'&isKI=%s' % self.isKI)	
		
		self._setPostdata(postdata)
		return c._postData()		
		
	def removeHTAbove(self):
		'''
		Use this interface to remove a threshold violation event 
		Optional sourceAdapter parameter specifies the adapter that is removing the event. 
		If sourceAdapter is not specified "Http Post" adapter is used. 
		'''

		postdata = (u'action=removeHTAbove')
		if (self.sourceAdapter)		: postdata += (u'&sourceAdapter=%s' % self.sourceAdapter)
		if (self.resourceName)		: postdata += (u'&resourceName=%s' % self.resourceName)
		if (self.adapterKindKey)	: postdata += (u'&adapterKindKey=%s' % self.adapterKindKey)
		if (self.resourceKindKey)	: postdata += (u'&resourceKindKey=%s' % self.resourceKindKey)
		if (self.identifiers)		: postdata += (u'&identifiers=%s' % self.identifiers)
		if (self.metricName)		: postdata += (u'&metricName=%s' % self.metricName)
		if (self.abnormalityCancelTime): postdata += (u'&cancelTime=%s' % self.abnormalityCancelTime)
		
		self._setPostdata(postdata)
		return c._postData()		

	def addHTBelow(self):
		'''
		Use this interface to push externally detected threshold violation event 
		for a particular metric of a particular resource (All fields are required) 
		Effects: if resource does not exist, it is created with resourceKind and adapterKind given; 
		if the adapterKind does not exist, it is created;
		if the resourceKind does not exist, it is created; 
		if the resourceKind does not contain an attribute with the name specified by metricName, it is created 
		Optional sourceAdapter parameter specifies the adapter that is sending the event. 
		If sourceAdapter is not specified "Http Post" adapter is used. 
		'''
		
		postdata = (u'action=addHTBelow')
		if (self.sourceAdapter) 	: postdata += (u'&sourceAdapter=%s' % self.sourceAdapter)
		if (self.resourceName)		: postdata += (u'&resourceName=%s' % self.resourceName)
		if (self.adapterKindKey)	: postdata += (u'&adapterKindKey=%s' % self.adapterKindKey)
		if (self.resourceKindKey)	: postdata += (u'&resourceKindKey=%s' % self.resourceKindKey)
		if (self.identifiers)		: postdata += (u'&identifiers=%s' % self.identifiers)
		if (self.metricName)		: postdata += (u'&metricName=%s' % self.metricName)	
		if (self.abnormalityTime)	: postdata += (u'&time=%s' % self.abnormalityTime)
		if (self.values)			: postdata += (u'&value=%s' % self.values)		
		if (self.abnormalityMessage): postdata += (u'&message=%s' % self.abnormalityMessage)			
		if (self.managedExternally)	: postdata += (u'&managedExternally=%s' % self.managedExternally)	
		if (self.isKI)				: postdata += (u'&isKI=%s' % self.isKI)	
		
		self._setPostdata(postdata)
		return c._postData()		
		
	def removeHTBelow(self):
		'''
		Use this interface to remove a threshold violation event 
		Optional sourceAdapter parameter specifies the adapter that is removing the event. 
		If sourceAdapter is not specified "Http Post" adapter is used. 
		'''

		postdata = (u'action=removeHTBelow')
		if (self.sourceAdapter)		: postdata += (u'&sourceAdapter=%s' % self.sourceAdapter)
		if (self.resourceName)		: postdata += (u'&resourceName=%s' % self.resourceName)
		if (self.adapterKindKey)	: postdata += (u'&adapterKindKey=%s' % self.adapterKindKey)
		if (self.resourceKindKey)	: postdata += (u'&resourceKindKey=%s' % self.resourceKindKey)
		if (self.identifiers)		: postdata += (u'&identifiers=%s' % self.identifiers)
		if (self.metricName)		: postdata += (u'&metricName=%s' % self.metricName)	
		if (self.abnormalityCancelTime): postdata += (u'&cancelTime=%s' % self.abnormalityCancelTime)
		
		self._setPostdata(postdata)
		return c._postData()		
		
	def addHTEquals(self):
		'''
		Use this interface to push externally detected threshold violation event 
		for a particular metric of a particular resource (All fields are required) 
		Effects: if resource does not exist, it is created with resourceKind and adapterKind given; 
		if the adapterKind does not exist, it is created; 
		if the resourceKind does not exist, it is created; 
		if the resourceKind does not contain an attribute with the name specified by metricName, it is created 
		Optional sourceAdapter parameter specifies the adapter that is sending the event. 
		If sourceAdapter is not specified "Http Post" adapter is used
		'''

		postdata = (u'action=addHTEquals')
		if (self.sourceAdapter)		: postdata += (u'&sourceAdapter=%s' % self.sourceAdapter)
		if (self.resourceName)		: postdata += (u'&resourceName=%s' % self.resourceName)
		if (self.adapterKindKey) 	: postdata += (u'&adapterKindKey=%s' % self.adapterKindKey)
		if (self.resourceKindKey)	: postdata += (u'&resourceKindKey=%s' % self.resourceKindKey)
		if (self.identifiers)		: postdata += (u'&identifiers=%s' % self.identifiers)
		if (self.metricName)		: postdata += (u'&metricName=%s' % self.metricName)	
		if (self.abnormalityTime)	: postdata += (u'&time=%s' % self.abnormalityTime)
		if (self.values)			: postdata += (u'&value=%s' % self.values)	
		if (self.abnormalityMessage): postdata += (u'&message=%s' % self.abnormalityMessage)			
		if (self.managedExternally)	: postdata += (u'&managedExternally=%s' % self.managedExternally)	
		if (self.isKI)				: postdata += (u'&isKI=%s' % self.isKI)
		
		self._setPostdata(postdata)
		return c._postData()	

	def removeHTEquals(self):
		'''
		Use this interface to remove a threshold violation event 
		Optional sourceAdapter parameter specifies the adapter that is removing the event. 
		If sourceAdapter is not specified "Http Post" adapter is used. 
		'''
		
		postdata = (u'action=removeHTEquals')
		if (self.sourceAdapter)		: postdata += (u'&sourceAdapter=%s' % self.sourceAdapter)
		if (self.resourceName)		: postdata += (u'&resourceName=%s' % self.resourceName)
		if (self.adapterKindKey)	: postdata += (u'&adapterKindKey=%s' % self.adapterKindKey)
		if (self.resourceKindKey)	: postdata += (u'&resourceKindKey=%s' % self.resourceKindKey)
		if (self.identifiers)		: postdata += (u'&identifiers=%s' % self.identifiers)
		if (self.metricName)		: postdata += (u'&metricName=%s' % self.metricName)	
		if (self.abnormalityCancelTime)	: postdata += (u'&cancelTime=%s' % self.abnormalityCancelTime)
		
		self._setPostdata(postdata)
		return c._postData()		
		
	def addHTNotEqual(self):
		'''
		Use this interface to push externally detected threshold violation event 
		for a particular metric of a particular resource (All fields are required) 
		Effects: if resource does not exist, it is created with resourceKind and adapterKind given; 
		if the adapterKind does not exist, it is created; 
		if the resourceKind does not exist, it is created; 
		if the resourceKind does not contain an attribute with the name specified by metricName, it is created 
		Optional sourceAdapter parameter specifies the adapter that is sending the event. 
		If sourceAdapter is not specified "Http Post" adapter is used. 
		'''

		postdata = (u'action=addHTNotEqual')
		if (self.sourceAdapter)		: postdata += (u'&sourceAdapter=%s' % self.sourceAdapter)
		if (self.resourceName)		: postdata += (u'&resourceName=%s' % self.resourceName)
		if (self.adapterKindKey)	: postdata += (u'&adapterKindKey=%s' % self.adapterKindKey)
		if (self.resourceKindKey)	: postdata += (u'&resourceKindKey=%s' % self.resourceKindKey)
		if (self.identifiers)		: postdata += (u'&identifiers=%s' % self.identifiers)
		if (self.metricName)		: postdata += (u'&metricName=%s' % self.metricName)	
		if (self.abnormalityTime)	: postdata += (u'&time=%s' % self.abnormalityTime)
		if (self.values)			: postdata += (u'&value=%s' % self.values)	
		if (self.abnormalityMessage): postdata += (u'&message=%s' % self.abnormalityMessage)			
		if (self.managedExternally)	: postdata += (u'&managedExternally=%s' % self.managedExternally)	
		if (self.isKI)				: postdata += (u'&isKI=%s' % self.isKI)
		
		self._setPostdata(postdata)
		return c._postData()			
		
	def removeHTNotEqual(self):
		'''
		Use this interface to remove a threshold violation event 
		Optional sourceAdapter parameter specifies the adapter that is removing the event. 
		If sourceAdapter is not specified "Http Post" adapter is used. 
		'''
		
		postdata = (u'action=removeHTNotEqual')
		if (self.sourceAdapter)		: postdata += (u'&sourceAdapter=%s' % self.sourceAdapter)
		if (self.resourceName)		: postdata += (u'&resourceName=%s' % self.resourceName)
		if (self.adapterKindKey)	: postdata += (u'&adapterKindKey=%s' % self.adapterKindKey)
		if (self.resourceKindKey)	: postdata += (u'&resourceKindKey=%s' % self.resourceKindKey)
		if (self.identifiers)		: postdata += (u'&identifiers=%s' % self.identifiers)
		if (self.metricName)		: postdata += (u'&metricName=%s' % self.metricName)	
		if (self.abnormalityCancelTime): postdata += (u'&cancelTime=%s' % self.abnormalityCancelTime)
		
		self._setPostdata(postdata)
		return c._postData()		
		
	def configureAttributeThresholds(self):
		'''
		To do 
		Use this interface to configure the thresholds of the specified attribute 

		action="configureAttributeThresholds&,%s"

		where value of %s can be


		[resourceName],[adapterKind],[resourceKind],[identifiers],[attributeKey],[isDTAboveKI],[isDTBelowKI],[isHardThresholdKI],[criticalityLevel],\n 
		[criticality],[htCompare],[value],[waiteCycle],[cancelCycle],\n 
		[criticality],[htCompare],[value],[waiteCycle],[cancelCycle],\n 
		etc.. 

		or


		[adapterKind],[resourceKind],[attributePackage],[attributeKey],[isDTAboveKI],[isDTBelowKI],[isHardThresholdKI],[criticalityLevel],\n 
		[criticality],[htCompare],[value],[waiteCycle],[cancelCycle],\n 
		[criticality],[htCompare],[value],[waiteCycle],[cancelCycle],\n 
		etc.. 
		'''
		return ('None')
		
	def addGeoLocation(self):
		'''
		Use this interface to add new GEO location and assign given resources to it. 
		If no resource is provided, an empty GEO location will be created. 
		'''
		
		postdata = (u'action=addGeoLocation')
		if (self.geoLocationName) 	: postdata += (u'&geoLocationName=%s' % self.geoLocationName)
		if (self.latitude)			: postdata += (u'&latitude=%s' % self.latitude)
		if (self.longitude) 		: postdata += (u'&longitude=%s' % self.longitude)
		if (self.resources)			: postdata += (u'&resources=%s' % self.resources)
		
		self._setPostdata(postdata)
		return c._postData()	
	
	def getResourceState(self):
		'''
		Use this interface to get the state of the resource against given source adapter instance. 
		Optional sourceAdapter parameter specifies the adapter that is going to send data for the resource. If sourceAdapter is not specified "Http Post" adapter is used. 
		Return values:
			Started - when the resource is started
			Stopped - for stopped resources
			No adapter instance - specified adapter instance does not exist
			Stopped adapter instance - specified adapter instance is not started
			Unknown - the resource is not attached to given adapter instance.
		'''
		
		postdata = (u'action=getResourceState')
		if (self.sourceAdapter) 	: postdata += (u'&sourceAdapter=%s' % self.sourceAdapter)
		if (self.resourceName)		: postdata += (u'&resourceName=%s' % self.resourceName)
		if (self.adapterKindKey)	: postdata += (u'&adapterKindKey=%s' % self.adapterKindKey)
		if (self.resourceKindKey)	: postdata += (u'&resourceKindKey=%s' % self.resourceKindKey)
		if (self.identifiers)		: postdata += (u'&identifiers=%s' % self.identifiers)
		
		self._setPostdata(postdata)
		return c._postData()	
	
	def lookupResource(self):
		'''
		Use this interface to find existing resources matching specified resource name, adapter kind and resource kind. 
		Resource name matching can use string compare or regular expression matching. 
		To enable regular expression matching specify "regex:" prefix followed by the matching pattern. 
		Adapter kind and resource kind parameters are optional. 
		If not specified only name will be used for matching. 
		Return value is one row per found resource: 
			resourceName=[name of resource]&adapterKindKey=[adapterKindKey]&resourceKindKey=[resourceKindKey]&identifiers=[identifiers]
		'''

		postdata = (u'action=lookupResource')
		if (self.sourceAdapter)		: postdata += (u'&sourceAdapter=%s' % self.sourceAdapter)
		if (self.resourceName)		: postdata += (u'&resourceName=%s' % self.resourceName)
		if (self.adapterKindKey)	: postdata += (u'&adapterKindKey=%s' % self.adapterKindKey)
		if (self.resourceKindKey) 	: postdata += (u'&resourceKindKey=%s' % self.resourceKindKey)
		
		self._setPostdata(postdata)
		return c._postData()	

	def getRelationships(self):
		'''
		Use this interface to get relationships for resources matching given resource name, adapter kind and resource kind. 
		Resource name can contain SQL style wild cards, i.e. '%' stands for any number of occurrences of any character, 
		'_' - single occurrence, etc. Backslash ('\') is an escape character, 
		so in order to lookup a resource that has special characters in the name, e.g. '\', '%' and '_', 
		they should be escaped with a preceding '\' character. 
		
		Adapter kind and resource kind parameters are optional. If not specified only name will be used for matching. 
		
		getParents and getChildren parameters control whether the relationships tree will be walked up and/or down. 
		If not specified only direct children will be returned. 

		Return value for each matching resource can contain multiple lines separated by 5 dashes (-----). 

		Every section contains a resource key an the first line followed by Parents section and Children section. 

		Parents section is staring with Parents: keyword in the first line. All subsequent lines contain parent resource keys. 
		The section is ended by the beginning of another section. 

		Children section is staring with Children: keyword in the first line. 
		All subsequent lines contain child resource keys. 
		The section is ended by the beginning of another section. 

		Every resource key is one row per resource: 
			resourceName=[name of resource]&adapterKindKey=[adapterKindKey]&resourceKindKey=[resourceKindKey]&identifiers=[identifiers]
		'''
	
		postdata = (u'action=getRelationships')
		if (self.resourceName) 		: postdata += (u'&resourceName=%s' % self.resourceName)
		if (self.adapterKindKey)	: postdata += (u'&adapterKindKey=%s' % self.adapterKindKey)
		if (self.resourceKindKey)	: postdata += (u'&resourceKindKey=%s' % self.resourceKindKey)
		if (self.identifiers) 		: postdata += (u'&identifiers=%s' % self.identifiers)
		if (self.getParents) 		: postdata += (u'&getParents=%s' % self.getParents)
		if (self.getChildren)		: postdata += (u'&getChildren=%s' % self.getChildren)
		
		
		self._setPostdata(postdata)
		return c._postData()	
	
	def getMetricDataAndDT(self):
		'''
		Use this interface to get collected data for a resource and a metric. 
		Results will be a CSV List (Including the header):

		Time, Value, LowDT, HighDt, smooth
		1365195172879, 37.5, 15.2, 73.3, 36.2 -- with DT and Smooth values
		1365195172879, 37.5, , , 36.2 -- with no dt and smooth values
		1365195172879, 37.5, , , -- with no dt and no smooth
		'''
	
		postdata = (u'action=getMetricDataAndDT')
		if (self.resourceName) 		: postdata += (u'&resourceName=%s' % self.resourceName)
		if (self.adapterKindKey)	: postdata += (u'&adapterKindKey=%s' % self.adapterKindKey)
		if (self.resourceKindKey) 	: postdata += (u'&resourceKindKey=%s' % self.resourceKindKey)
		if (self.identifiers)		: postdata += (u'&identifiers=%s' % self.identifiers)
		if (self.metricKey) 		: postdata += (u'&metricKey=%s' % self.metricKey)
		if (self.starttime) 		: postdata += (u'&starttime=%s' % self.starttime)
		if (self.endtime) 			: postdata += (u'&endtime=%s' % self.endtime)
		if (self.includeDt) 		: postdata += (u'&includeDt=%s' % self.includeDt)
		if (self.includeSmooth) 	: postdata += (u'&includeSmooth=%s' % self.includeSmooth)
		
		self._setPostdata(postdata)
		return c._postData()	
	
	def handleDataFeed(self):
		'''
		To do, how to find out AdapterInstanceId??
		Use this interface to post adapter specific data to a Hybrid adapter. 
		Hybrid adapter is an adapter which is of type "internal" adapter but also relies on <handleDataFeed> method to receive data. 
		This data could be inventory data, time series data or alerts information. 
		It is assumed that the corresponding internal adapter is able to understand syntax and semantics of the data.
		'''

		postdata = (u'action=handleDataFeed')
		if (self.AdapterInstanceId) : postdata += (u'&AdapterInstanceId=%s' % self.AdapterInstanceId)
		if (self.adapterKindKey)	: postdata += (u'&adapterKindKey=%s' % self.adapterKindKey)		

		self._setPostdata(postdata)
		return c._postData()		
	
	def getMetricValuesFromMemory(self):
		'''
		Use this interface to get data for metrics of existing resources matching specified resource name, adapter kind and resource kind. 

		Resource key matching or regular expression matching by name. 
		To enable regular expression matching specify "regex:" prefix followed by the matching pattern. 
		For reg. exp. adapterKind and resourceKind parameters are optional, If not specified only name will be used for matching. 

		Results will be a CSV List (Including the header):


		ResourceKey,MetricKey, Time, Value

		{resourceName=Win-7-64-Dev&adapterKindKey=vmware&resourceKindKey=VirtualMachine}, vm|mem|guest_demand, 1364230860547, 0.0

		'''
	
		postdata = (u'action=getMetricValuesFromMemory')
		if (self.resources) : postdata += (u'&resources=%s' % self.resources)
		if (self.metricKeys) : postdata += (u'&metricKeys=%s' % self.metricKeys)
		self._setPostdata(postdata)
		return c._postData()	
		
	def _postData(self):

		try:
			cj = http.cookiejar.CookieJar()
			urllib.request.HTTPCookieProcessor(cj)
			auth_handler = urllib.request.HTTPBasicAuthHandler()
			auth_handler.add_password(realm = self.auth_realm,
								  uri = self.url,
								  user = self.username,
								  passwd = self.password)
			opener = urllib.request.build_opener(auth_handler)
			# ...and install it globally so it can be used with urlopen.
			urllib.request.install_opener(opener)
			# print (self.postdata.encode('ascii'))
			f = urllib.request.urlopen(self.url, bytes(self.postdata, 'utf-8'))
			return f.read().decode('utf-8')
				
		except urllib.request.HTTPError as http_error:
			return ('Error: ' + str(http_error.code) +' ' + http_error.reason)
		
if __name__ == "__main__":
	c = WebServletCtrol()
	c.setResKindKey('Test res')
	c.setMonitoringInt(5) 
	c.setResDescription('test test')
	c.setResName('test2')
	# c.setSourceAdapter()
	c.setMetricKey('Throughput|IO MB/s')
	c.setStarttime('2013/08/06 15:00:00')
	print (c.getMetricDataAndDT())
	
	########################################	
	# c.setResKindKey('VirtualMachine')
	# c.setResName('VM_test')
	# c.setResDescription('VMTest')
	c.setMetricName('Throughput|IO MB/s')
	# c.setIdentifiers('VMEntityName::12::false$$VMEntityObjectID::443$$VMEntityVCID::222')
	c.addMetricData('Throughput|IO MB/s','4','NoValue', '2013/08/06 15:00:00', '30')
	c.addMetricData('Throughput|IO MB/s','0','NoValue', '2013/08/06 15:05:00', '40')
	c.addMetricData('Throughput|IO MB/s','1','NoValue', '2013/08/06 15:10:00', '50')
	c.addMetricData('Throughput|IO MB/s','2','NoValue', '2013/08/06 15:15:00', '60')
	c.addMetricData('Throughput|IO MB/s','3','NoValue', '2013/08/06 15:20:00', '70')
	c.addMetricData('Throughput|IO MB/s','4','NoValue', '2013/08/06 15:25:00', '80')
	c.addMetricData('Throughput|IO MB/s','0','NoValue', '2013/08/06 15:30:00', '90')
	c.addMetricData('Throughput|IO MB/s','1','NoValue', '2013/08/06 15:35:00', '100')
	c.addMetricData('Throughput|IO MB/s','2','NoValue', '2013/08/06 15:40:00', '100')
	c.addMetricData('Throughput|IO MB/s','3','NoValue', '2013/08/06 15:45:00', '100')
	c.addMetricData('Throughput|IO MB/s','3','NoValue', '2013/08/06 15:50:00', '30')
	c.addMetricData('Throughput|IO MB/s','3','NoValue', '2013/08/06 15:55:00', '40')
	c.addMetricData('Throughput|IO MB/s','3','NoValue', '2013/08/06 16:10:00', '50')
	c.addMetricData('Throughput|IO MB/s','3','NoValue', '2013/08/06 16:15:00', '60')
	c.addMetricData('Throughput|IO MB/s','3','NoValue', '2013/08/06 16:20:00', '70')
	c.addMetricData('Throughput|IO MB/s','3','NoValue', '2013/08/06 16:25:00', '80')
	c.addMetricData('Throughput|IO MB/s','3','NoValue', '2013/08/06 16:30:00', '90')
	c.addMetricData('Throughput|IO MB/s','3','NoValue', '2013/08/06 16:35:00', '100')
	c.addMetricData('Throughput|IO MB/s','3','NoValue', '2013/08/06 16:35:00', '10')
	c.addMetricData('Throughput|IO MB/s','3','NoValue', '2013/08/06 16:45:00', '20')
	# print (c.metricsList)
	print (c.addGeneralMetricObservations())
	
	##########################################
	c.addProperty('others','2013/08/06 15:00:00','1')
	c.addProperty('package','2013/08/06 15:20:00','2')
	c.addProperty('data','2013/08/06 15:30:00','3')
	c.addProperty('time','2013/08/06 15:40:00','4')
	c.addProperty('size','2013/08/06 15:50:00','5')
	c.addProperty('color','2013/08/06 15:55:00','6')	
	print (c.addPropertyData())
	
	##########################################
	# c.setResKindKey('DATACENTER')
	# c.setResName('HOST2')
	# c.setMetricName('AVERAGE_HOST_CPU_CAPACITY_MHZ')	
	# c.setMonitoringInt(5)
	# print (c.openResource())
	#print (c.stopResource())
	##########################################
	
	print (c.getMonitoringResources())
	
	
	###########################################
	#  remove resource
	#############################################
		
	# c.setResKindKey('WORLD')
	# c.setResName('Test_World')
	# c.stopResource()
	# print (c.removeResourceFromAdapterInstance())	
	
	# c.setResKindKey('World')
	# c.setResName('Test_World2')
	# c.setIdentifiers('VMEntityName::12::false$$VMEntityObjectID::443$$VMEntityVCID::222')
	# c.stopResource()
	# print (c.removeResourceFromAdapterInstance())	
		