/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <string>

using namespace std;

class Animal {
private:
    bool isMammal;
    bool isCarni;
public:
    Animal(bool isMammal, bool isCarni){
        isMammal = isMammal;
        isCarni = isCarni;
    }
    
    bool getIsMammal(){
        return isMammal;
    }
    
    bool getIsCarni(){
        return isCarni;
    }
    
    virtual string getGreeting() = 0;
    
    void printAnimal(string name){
        cout << "A " << name << "says " << this->getGreeting() << ", " 
        << "is" << (this->getIsMammal() ? " " : " not ") << "mammal,"
        << "is" << (this->getIsCarni() ? " " : " not ") << "carni." << endl;
    }
        
};

class Dog: public Animal{
public:
    Dog(): Animal(true, false){}
    virtual string getGreeting(){
        return "ruff";
    } 
};

class Cow: public Animal{
public:
    Cow(): Animal(true, true){}
    virtual string getGreeting(){
        return "moo";
    } 
};

class Duck: public Animal{
public:
    Duck(): Animal(false, false){}
    virtual string getGreeting(){
        return "quack";
    }
};

int main()
{
    Dog dog;
    Animal * prt = &dog;
    prt->printAnimal("dog");
    
    Cow cow;
    prt = &cow;
    prt->printAnimal("cow");
    
    Duck duck;
    prt = &duck;
    prt->printAnimal("duck");
    
}
