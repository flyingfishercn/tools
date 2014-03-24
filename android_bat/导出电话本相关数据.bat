

adb pull data/data/com.android.providers.contacts/databases/contacts2.db Contacts\contacts2.db
adb pull data/data/com.android.providers.contacts/databases/profile.db Contacts\profile.db
adb pull data/data/com.android.providers.contacts/shared_prefs/ContactsUpgradeReceiver.xml Contacts\ContactsUpgradeReceiver.xml
adb pull data/data/com.android.providers.contacts/shared_prefs/com.android.providers.contacts_preferences.xml Contacts\com.android.providers.contacts_preferences.xml

adb pull data/data/com.android.providers.contacts/files/photos Contacts\phtotos

adb pull data/data/com.android.providers.telephony/databases/telephony.db Contacts\telephony.db

adb pull data/data/com.android.providers.settings/databases/settings.db Contacts\settings.db

adb pull data/data/com.android.contacts/shared_prefs/sim_contacts_ready.xml Contacts\sim_contacts_ready.xml
pause