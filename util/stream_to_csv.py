import os
import csv

class Stream_To_CSV():
    def __init__(self, path):
        # path to csv
        self.path = path

    def process_payload(self, data):
        # Take dictionary object passed in and convert it into data for writer.writerow()
        payload = []
        for record in data:
            payload.append([
                record['created'].split('T')[0],
                record['lastmodified'].split('T')[0],
                record['emailaddress'],
                record['firstname'],
                record['lastname'],
                record['title'],
                record['work_phone'],
                record['mobile_phone'],
                record['home_phone'],
                record['other_phone'],
                record['stat_inboundemails'],
                record['stat_outboundemails'],
                record['address_street'],
                record['address_city'],
                record['address_state'],
                record['address_postalcode'],
                record['address_country'],
                record['location_city'],
                record['location_state'],
                record['location_zipcode'],
                record['location_country'],
                record['isspam'],
                ','.join(record['sources'])
            ])
        return payload

    def write_to_csv(self, data):
        payload = self.process_payload(data)
        with open(self.path, 'a', newline='') as file:
            fw = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL, quotechar='"')
            fw.writerows(payload)
