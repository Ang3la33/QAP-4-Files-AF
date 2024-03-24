// Object containing attributes and methods for the Motel customer.
// Author: Angela Flynn

const customer = {
    fname: 'Bob',
    lname: 'Ross',
    bdate: new Date('1942-10-29'),
    gender: 'Male',
    pronouns: 'He/Him',
    phoneNo: '709-867-5309',
    email: 'happy_accidents@outlook.com',
    address: {
        street: '123 Happy Little Tree Lane',
        city: 'Holyrood',
        province: 'NL',
        postal: 'A0A2R0',
        country: 'CANADA',
    },
    reservation: {
        checkIn: new Date('2024-01-10'),
        checkOut: new Date('2024-01-16'),
    },
    roomPreference: ['King Bed', 'Ocean View', 'Even room number', 'Art easel', 'MnM\'s - but only the green ones'],
    payMethod: 'Visa',
    // This function will calculate the customer's age by taking the current date and subtracting the customer's birth date. 
    // It will also check if the current dates month and/or day are before or after the birth dates month and/or day.This step
    // is important! For instance, my birth date is August 16th, 1990 and I will remain 33 until the end of that day! However,
    // if you were to subtract this year(2024) by my birth year(1990) the answer would be 34 and I would not be happy to age 
    // sooner than August! Therefore, the if/else statement would apply to me and 'age--' would subtract a year off leaving 
    // my age at 33 until August 16th! phew! 
    getAge: function calculateAge() {
        var today = new Date();
        var bdate = new Date(this.bdate);
        var age = today.getFullYear() - bdate.getFullYear();
        var month = today.getMonth() - bdate.getMonth();
        if (month < 0 || (month === 0 && today.getDate() < bdate.getDate())){
            age--;
        }
        return age;
    },
    // This function will take the check-out date and subtract the check-in date. This will leave you with the duration 
    // of the customer's stay at the Motel. I have also chosen to subtract a day as generally Motel's charge by the night.
    getDuration: function durationOfStay() {
        var stay = this.reservation.checkOut.getDate() - this.reservation.checkIn.getDate();
        var duration = stay - 1; 
        return duration
    }
} 

console.log(customer);
let age = customer.getAge();
let duration = customer.getDuration();

const roomPreference = ['King Bed', 'Ocean View', 'Even room number', 'Art easel', 'MnM\'s - but only the green ones'];
const roomPreferenceList = roomPreference.map(roomPreference => `<li>${roomPreference}</li>`).join('');

storyOfBob = `Mr. ${customer.fname} ${customer.lname} is an honored guest here at Sleep-Tite Motel. ${customer.fname}'s gender is ${customer.gender} and ${customer.fname}'s pronouns
are ${customer.pronouns}. He is ${age} years of age and requires a wake-up call at 7am sharp on his cell: ${customer.phoneNo}. Mr. ${customer.lname} will be staying 
with us for ${duration} nights. Mr. ${customer.lname} has requested his receipt be emailed to him at ${customer.email}, as he is a very eco-conscious man. ${customer.fname} has been kind enough to pay upfront using ${customer.payMethod}. Therefore, we are more than happy to 
accommodate his room preferences. Please review the list below before ${customer.fname}'s visit:
<ul>
    ${roomPreferenceList}
</ul>`;

console.log(storyOfBob);

document.body.innerHTML = storyOfBob;



