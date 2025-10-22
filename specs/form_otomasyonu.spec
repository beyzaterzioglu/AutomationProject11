#Specification Heading

Created by beyza on 2.10.2025

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

## TC1 - Form sayfasını açmak

tags: form, pozitif
* Form sayfası açılır

## TC2 - Name alanına text yazmak

tags: form, pozitif
* Form sayfası açılır
* "FirstNameInput" alanına "name" degerini yaz.

## TC3 - Name alanına sayı yazmak

tags: form
* Form sayfası açılır
* "FirstNameInput" alanına "number" degerini yaz.

## TC4 - Name alanına özel karakter yazmak

tags: form
* Form sayfası açılır
* "FirstNameInput" alanına "character" degerini yaz.

## TC5 - Last Name alanına text yazmak

tags: form
* Form sayfası açılır
* "LastNameInput" alanına "lastName" degerini yaz.

## TC6 - Last Name alanına sayı yazmak

tags: form
* Form sayfası açılır
* "LastNameInput" alanına "number" degerini yaz.

## TC7 - Last Name alanına özel karakter yazmak

tags: form
* Form sayfası açılır
* "LastNameInput" alanına "character" degerini yaz.

## TC8 - Email alanına mail yazmak

tags: form, pozitif
* Form sayfası açılır
* "EmailInput" alanına "email" degerini yaz.


## TC9 - Email alanına text yazmak
tags: form
* Form sayfası açılır
* "EmailInput" alanına "text" degerini yaz.

## TC10 - Email alanına sayı yazmak
tags: form
* Form sayfası açılır
* "EmailInput" alanına "number" degerini yaz.

## TC11 - Email alanına özel karakter yazmak

tags: form
* Form sayfası açılır
* "EmailInput" alanına "character" degerini yaz.

## TC12 - Cinsiyet seçimi yapmak
tags: form, pozitif
* Form sayfası açılır
* "FemaleGender" alanına tıklanır

## TC13 -Mobile alanına 10 haneli numara girmek
tags: form, pozitif
* Form sayfası açılır
* "MobileNumber" alanına "10DigitMobile" degerini yaz.

## TC14 - Mobile alanına 10 haneli text girmek
tags: form
* Form sayfası açılır
* "MobileNumber" alanına "10DigitText" degerini yaz.

## TC15 - Doğum tarihi seçimi yapmak
tags: form,pozitif
* Form sayfası açılır
* Doğum tarihi seçilir

## TC16 - Subjects alanına text girişi yapmak
tags: form
* Form sayfası açılır
* "SubjectField" alanına "subject1" degerini yaz.

## TC17 - Subjects alanına sayı girişi yapmak
tags: form
* Form sayfası açılır
* "SubjectField" alanına "number" degerini yaz.

## TC18 - Hobi seçimi yapmak
tags: form,pozitif
* Form sayfası açılır
* "HobbyReading" alanına tıklanır

## TC19 - Birden fazla hobi seçimi yapmak
tags: form,pozitif
* Form sayfası açılır
* "HobbyReading" alanına tıklanır
* "HobbyMusic" alanına tıklanır

## TC20 - Dosya seçmek
tags: form,pozitif
* Form sayfası açılır
* Dosya seçimi yapılır


## TC21 - Adres girişi yapmak
tags: form,pozitif
* Form sayfası açılır
* "CurrentAddress" alanına "currentAddress" degerini yaz.

## TC22 - State seçimi yapmak
tags: form,pozitif
* Form sayfası açılır
* State seçimi yapılır.

## TC23 - City seçimi yapmak
tags: form,pozitif
* Form sayfası açılır
* State seçimi yapılır.
* City seçimi yapılır.

## TC24 - Aynı anda iki cinsiyet seçimi yapmak
tags: form,negatif
* Form sayfası açılır
* "FemaleGender" alanına tıklanır
* "OtherGender" alanına tıklanır

## TC25 - Mobile alanına 10'den büyük uzunlukta numara girmek

tags: form,negatif
* Form sayfası açılır
* "MobileNumber" alanına "longPhoneNumber" degerini yaz.

## TC26 - Mobile alanına 10 haneden az numara girmek
tags: form,negatif
* Form sayfası açılır
* "MobileNumber" alanına "shortPhoneNumber" degerini yaz.

## TC27 - Mobile alanına 10'den büyük uzunlukta text girmek
tags: form,negatif
* Form sayfası açılır
* "MobileNumber" alanına "longPhoneNumber" degerini yaz.

## TC28 - Mobile alanına 10'dan az text girmek
tags: form,negatif
* Form sayfası açılır
* "MobileNumber" alanına "text" degerini yaz.

## TC29 - Gelecekte olan doğum tarihi seçimi yapmak
tags: form,negatif
* Form sayfası açılır
* Gelecekte olan bir doğum tarihi seçilir

## TC30 - Alanlar boşken submit butonuna tıklamak
tags: form,negatif
* Form sayfası açılır
* Kayıt işleminin onaylanmadığı doğrulanır


## TC31 - Formda zorunlu alanları doldurmak
tags: form,pozitif
* Form sayfası açılır
* "FirstNameInput" alanına "name" degerini yaz.
* "LastNameInput" alanına "lastName" degerini yaz.
* "EmailInput" alanına "email" degerini yaz.
* "FemaleGender" alanına tıklanır
* "MobileNumber" alanına "10DigitMobile" degerini yaz.
* "SubmitButton" alanına tıklanır
* Kayıt işlemin onaylandığı "header" başlığına bakarak doğrulanır

## TC32 - İsim alanını boş bırakarak submit butonuna tıklamak
tags: form,negatif
* Form sayfası açılır
* "LastNameInput" alanına "lastName" degerini yaz.
* "EmailInput" alanına "email" degerini yaz.
* "FemaleGender" alanına tıklanır
* "MobileNumber" alanına "10DigitMobile" degerini yaz.
* "SubmitButton" alanına tıklanır
* Kayıt işleminin onaylanmadığı doğrulanır

## TC33 - Soyisim alanını boş bırakarak submit butonuna tıklamak
tags: form,negatif
* Form sayfası açılır
* "FirstNameInput" alanına "name" degerini yaz.
* "EmailInput" alanına "email" degerini yaz.
* "FemaleGender" alanına tıklanır
* "MobileNumber" alanına "10DigitMobile" degerini yaz.
* "SubmitButton" alanına tıklanır
* Kayıt işleminin onaylanmadığı doğrulanır

## TC34 - Cinsiyet alanını boş bırakarak submit butonuna tıklamak
tags: form,negatif
* Form sayfası açılır
* "FirstNameInput" alanına "name" degerini yaz.
* "LastNameInput" alanına "lastName" degerini yaz.
* "EmailInput" alanına "email" degerini yaz.
* "MobileNumber" alanına "10DigitMobile" degerini yaz.
* "SubmitButton" alanına tıklanır
* Kayıt işleminin onaylanmadığı doğrulanır

## TC35 - Numara alanını boş bırakarak submit butonuna tıklamak
tags: form,negatif
* Form sayfası açılır
* "FirstNameInput" alanına "name" degerini yaz.
* "LastNameInput" alanına "lastName" degerini yaz.
* "EmailInput" alanına "email" degerini yaz.
* "FemaleGender" alanına tıklanır
* "SubmitButton" alanına tıklanır
* Kayıt işleminin onaylanmadığı doğrulanır


