//PROJECT BY:
//-ILAN HALIOUA (100472908)
//-LUCAS MONZÓN (100473232)

#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

//CLASSES AND SUBCLASSES:

class Employee{
	protected:
		string EmpName;
		string ID;
		string EmpAdress;
		string Telephone;
		double Salary;
		
	public:
		Employee (){
			EmpName = "";
			ID = "";
			EmpAdress = "";
			Telephone = "";
			Salary = 0;
		}
		
		Employee (string Ename, string id, string EA, string telephone, double salary){
			EmpName = Ename;
			ID = id;
			EmpAdress = EA;
			Telephone = telephone;
			Salary = salary;
		}
		
		void setEmpName(string Ename){
			EmpName = Ename;
		}
		string getEmpName(){
			return EmpName;
		}
		
		void setID(string id){
			ID = id;
		}
		string getID(){
			return ID;
		}
		
		void setEmpAdress(string EA){
			EmpAdress = EA;
		}
		string getEmpAdress(){
			return EmpAdress;
		}
		
		void setTelephone(string telephone){
			Telephone = telephone;
		}
		string getTelephone(){
			return Telephone;
		}
		
		void setSalary(double salary){
			Salary = salary;
		}
		double getSalary(){
			return Salary;
		}
};

class CentEmp: public Employee{
	private:
		string Occupation; //Cleaning, Administrations, Security, Customer service, Others...
		char type = 'C';
	public:
		CentEmp (): Employee(){
			Occupation = "";
			type = 'C';
		}
		CentEmp (string Ename, string id, string EA, string Telephone, double Salary, string ocup) : Employee(Ename, id, EA, Telephone, Salary){
			Occupation = ocup;
		}
		
		void setOccupation(string ocup){
			Occupation = ocup;
		}
		string getOccupation(){
			return Occupation;
		}
};

class StoreEmp: public Employee{
	private:
		string AssociatedStatus; // Manager or Staff
		char type = 'S';
	public:
		StoreEmp (): Employee(){
			AssociatedStatus = "";
			type = 'S';
		}	
		StoreEmp (string Ename, string id, string EA, string Telephone, double Salary, string AS): Employee(Ename, id, EA, Telephone, Salary){
			AssociatedStatus = AS;
		}
		
		void setAssociatedStatus(string AS){
			AssociatedStatus = AS;
		}
		string getAssociatedStatus(){
			return AssociatedStatus;
		}
};

class Product{
	private:
		string ProdName;
		string ProdID;
		float Price;
	public:
		Product (){
			ProdName = "";
			ProdID = "";
			Price = 0;
		}
		Product (string pname, string pid, float prc){
			ProdName = pname;
			ProdID = pid;
			Price = prc;
		}
		
		void setProdName(string pname){
			ProdName = pname;
		}
		string getProdName(){
			return ProdName;
		}
		
		void setProdID(string pid){
			ProdID = pid;
		}
		string getProdID(){
			return ProdID;
		}
		
		void setPrice(float prc){
			Price = prc;
		}
		float getPrice(){
			return Price;
		}
};

class Store{
	private:
		string StName;
		string StoreID;
		string Area;
		string Status;
		vector<class StoreEmp> StEmps; 
		vector<class Product> Catalogue;
	public:
		Store () {
			StName = "";
			StoreID = "";
			Area = ""; 
			Status = "";
		}
		Store (string sname, string sid, string area, string stus, vector<class StoreEmp> stEmpsVectorCurrentStore, vector<class Product> prodsVectorCurrentStore) {
			StName = sname;
			StoreID = sid;
			Area = area;
			Status = stus;
			StEmps = stEmpsVectorCurrentStore;
			Catalogue = prodsVectorCurrentStore;
		}
		
		//SETTERS & GETTERS
		
		void setStName(string sname){
			StName = sname;
		}
		string getStName(){
			return StName;
		}
		
		void setStoreID(string sid){
			StoreID = sid;
		}
		string getStoreID(){
			return StoreID;
		}
		
		void setArea(string area){
			Area = area;
		}
		string getArea(){
			return Area;
		}
		
		void setStatus(string stus){
			Status = stus;
		}
		string getStatus(){
			return Status;
		}
		
		void setStEmps(vector<class StoreEmp> stEmpsVectorCurrentStore){
			StEmps = stEmpsVectorCurrentStore;
		}
		vector<class StoreEmp> getStEmps(){
			return StEmps;
		}
		
		
		void setCatalogue(vector<class Product> prodsVectorCurrentStore){
			Catalogue = prodsVectorCurrentStore;
		}
		vector<class Product> getCatalogue(){
			return Catalogue;
		}
	
		// METHODS (Used afterward in several functions)
		
		void setCatF(class Product p){ 
			Catalogue.push_back(p);
		}
		void eraseCatF(int k){ 
			Catalogue.erase(Catalogue.begin()+k);
		}
		
};

class Center{
	private:
		string Name;
		string Adress;
		int Npark;
		vector<class Store> STORES;
		vector<class CentEmp> CenterEmps;
		
	public:	
		Center(){
			Name = "";
			Adress = "";
			Npark = 0;
		}
		Center(string name, string adress, int npark, vector<class Store> stores, vector<class CentEmp> cemployees){
			Name = name;
			Adress = adress;
			Npark = npark;
			STORES = stores;
			CenterEmps = cemployees;
		}
		
		// SETTERS & GETTERS
		
		void setName(string name){
			Name = name;
		}
		string getName(){
			return Name;
		}
		
		void setAdress(string adress){
			Adress = adress;
		}
		string getAdress(){
			return Adress;
		}
		
		void setNpark(int npark){
			Npark = npark;
		}
		int getNpark(){
			return Npark;
		}
		
		void setSTORES(vector<class Store> stores){
			STORES = stores;
		}
		vector<Store> getSTORES(){
			return STORES;
		}
		
		void setCenterEmps(vector<class CentEmp> cemployees){
			CenterEmps = cemployees;
		}
		vector<class CentEmp> getCenterEmps(){
			return CenterEmps;
		}
		
		// METHODS (Used afterward in several functions)

		setNewProd(int n, class Product p){ 
			STORES[n].setCatF(p);
		}
		
		EraseProd(int n, int k){ 
			STORES[n].eraseCatF(k);
		}
		
		
};

//FUNCTION PROTOTYPES:

Center readInitialData();
vector <pair<string, string>> getAllEmployees(Center mall);
void showAllEmployees(vector <pair<string, string>> ewlist);
void showStorePriceGivenProduct(class Center mall);
void addProductInStore(class Center &mall);
void removeProductInStore(class Center &mall);
void showAllInformation(class Center mall);
void saveAllInformation(class Center mall);
char showMenu();

//MAIN FUNCTION:

int main(){
	Center mall;
	mall = readInitialData();
	
	char opt = showMenu();

	while (opt != '7'){
		cout << "\n" << endl;
		
		switch (opt){
		case '1':
			showAllEmployees(getAllEmployees(mall));
			break;
		case '2':
			showStorePriceGivenProduct(mall);
			break;
		case '3':
			addProductInStore(mall);
			break;
		case '4':
			removeProductInStore(mall);
			break;
		case '5':
			showAllInformation(mall);
			break;
		case '6':
			saveAllInformation(mall);
			break;
		}
				
		cout << "\n" << endl;
		opt = showMenu();
	}

	return 0;
}

//FUNCTIONS: 

Center readInitialData(){
	
	Center mall;
	
	// StoresInfo file read:
	
	vector<class Store> stores;
		
	ifstream sfile;
	sfile.open("StoresInfo.txt", ios::in);
	
	if (!sfile){
		cout<< "File does not exsit " << endl;
	}else{
		string Mark = ""; 
			
		while (!sfile.eof()){

			
			string stName;
			getline (sfile, stName); 
			
			string stID;
			getline (sfile, stID); 
		
			string stArea;
			getline (sfile, stArea); 
		
			string stStatus;
			getline (sfile, stStatus); 
			
			getline (sfile, Mark);
			
			vector<StoreEmp> stEmpsVectorCurrentStore;
			while (Mark.compare("**s_employee**") == 0){
				
				string empName;
				getline (sfile, empName);
				
				string empID;
				getline (sfile, empID);
				   
				string empAdress;
				getline(sfile,empAdress);
				
				string empTel;
				getline(sfile,empTel);
				
				double empSalary;
				sfile >> empSalary;
				sfile.ignore(1,'\n'); 
				
				string empAssStat;
				getline (sfile, empAssStat);
				
				StoreEmp currentStoreEmp(empName, empID, empAdress, empTel, empSalary, empAssStat);
				stEmpsVectorCurrentStore.push_back(currentStoreEmp);
				
				getline (sfile, Mark);
			}
							
			
			vector<class Product> prodsVectorCurrentStore;
			while (Mark.compare("**product**") == 0){
				
				string prName;
				getline (sfile, prName);
			
				string prID;
				getline (sfile, prID); 
				
				float prPrice;
				sfile >> prPrice;
				sfile.ignore(1,'\n');
				
				Product currentProd(prName, prID, prPrice);
				prodsVectorCurrentStore.push_back(currentProd);
			
				getline (sfile, Mark);
			}
			if (stEmpsVectorCurrentStore.empty() == 0 ){
				Store currentStore(stName, stID, stArea, stStatus, stEmpsVectorCurrentStore, prodsVectorCurrentStore);
				stores.push_back(currentStore);
			}
					
		}
	}
		
	sfile.close();
				
	// CenterInfo file read:
		
	vector<class CentEmp> cemployees;
		
	ifstream cfile;
	cfile.open("CenterInfo.txt", ios::in);
	
	if (!cfile){
		cout<< "File does not exsit " << endl;
			
	}else{
		string employeeMark = "";

		string cName;
		getline (cfile, cName);
		    
		string cAdress;
		getline(cfile,cAdress);
				
		int cNPark;
		cfile >> cNPark;
		cfile.ignore(1,'\n');
			
		while (!cfile.eof()){	
			getline (cfile, employeeMark);
			while (employeeMark.compare("**c_employee**") == 0){
				string empName;
				getline (cfile, empName);
					
				string empID;
				getline (cfile, empID);
				
				string empAdress;
				getline(cfile,empAdress);
					
				string empTel;
				getline(cfile,empTel);
					
				double empSalary;
				cfile >> empSalary;
				cfile.ignore(1,'\n'); 
					
				string empOcup;
				getline (cfile, empOcup);
				
				CentEmp currentCentEmp(empName, empID, empAdress, empTel, empSalary, empOcup);
				cemployees.push_back(currentCentEmp);
				
				getline (cfile, employeeMark);
			}
				
		}
		mall.setName(cName);
		mall.setAdress(cAdress); 
		mall.setNpark(cNPark);
		mall.setSTORES(stores);
		mall.setCenterEmps(cemployees);
	
	}
	
	cfile.close();
	

	return mall; 
}

char showMenu(){
	
	char opt;
	
	cout << "Choose an option: " << endl;
	
	cout << "1. Show all employees\n2. Get store and price of a given product\n3. Add products in store\n4. Remove product in store\n5. Show all information\n6. Save all information\n7. End program" << endl;
		
	try
	{
		cin >> opt;

    	if (opt < '1' || opt > '7')
        	throw 'E';
	}
	catch (char sError)
	{
    	cout << "\nYou must introduce a number between 1 and 7. Try again.";
	}
	
	return opt;
}

vector <pair<string, string>> getAllEmployees(Center mall){
	//return: List of pairs (empl-workplace) ordered alfabetically

	vector <pair<string, string>> ewlist;
	
	for (int i = 0; i < mall.getSTORES().size(); i++){ //for each STORE
		for (int j = 0; j < mall.getSTORES()[i].getStEmps().size(); j++){ //for each of its EMPLOYEES
			pair<string, string> p (mall.getSTORES()[i].getStEmps()[j].getEmpName(),"Store"); //pair: Name, Workplace
			ewlist.push_back(p);
		}
	}
	
	for (int k = 0; k < mall.getCenterEmps().size(); k++){ //for each of Center EMPLOYEE
		pair<string, string> p (mall.getCenterEmps()[k].getEmpName(),"Center"); //pair: Name, Workplace
		ewlist.push_back(p);
	}
	
	sort(ewlist.begin(), ewlist.end());
	
	return ewlist;
}

void showAllEmployees(vector <pair<string, string>> ewlist){
	//Print content from ewlist
	 
	cout << left << setw(25) << "EMPLOYEE NAME" << "WORKPLACE" << endl; //SETW(): Modifies the field width only for the next input or output. By default it is 0, but it expands as necessary (In this case -> 25).
	cout << "-----------------------------------" << endl;              
	
	vector <pair<string, string>>::iterator it;
	for(it = ewlist.begin(); it != ewlist.end(); it++){
		cout << left << setw(25) << (*it).first << (*it).second << endl;
	}

}

void showStorePriceGivenProduct(class Center mall){
	//ask product's name
	//print names of the stores that contain the product and its price
	
	string StoreName, ProdName, ProdID, ProdPrice;
	cout << "Introduce the NAME of the PRODUCT you want the price of: ";
	cin >> ProdName;
	
	for (int c = 0; c < ProdName.size(); c++){  // In order to print afterwards 'ProdName' in CAPITAL LETTERS.
		ProdName[c] = toupper(ProdName[c]); 
	}
		
	cout << "\n" << ProdName << endl;
	cout << "Store\t\tPrice" << endl;
	cout << "---------------------" << endl;
		
	
	int Pfound = 0;
	int prodpos = -1;
	
	for (int stpos = 0; stpos <mall.getSTORES().size(); stpos++){	//for each STORE
		for(int j = 0; j<mall.getSTORES()[stpos].getCatalogue().size(); j++){ //for each of its PRODUCTS
			if(strcasecmp(mall.getSTORES()[stpos].getCatalogue()[j].getProdName().c_str(), ProdName.c_str()) == 0){ //strcasecmp(): Compares strings ignoring their CASE. When strcasecmp(...,...) == 0, means when the 2 strings compared in the argument are the same.
				Pfound = 1;
				prodpos = j;
				cout << left << setw(16) << mall.getSTORES()[stpos].getStName() << mall.getSTORES()[stpos].getCatalogue()[j].getPrice() << endl; //print: Store NAME - PRICE of the product in that store
			}
		}
	}
	if (Pfound == 0){ // If product not found:
		cout << "\nNone of the stores in this center contains this product. We are sorry. Try with another product." << endl;
	}
	
}

void addProductInStore(Center &mall){
	//adds new prod in catalogue of a store:
	//Ask store and info o the new prod
	//Check prod does not already exist
	
	string StoreName, ProdName, ProdID; 
	float ProdPrice;
	
	cout << "Introduce the NAME of the STORE you want to add a new product to: ";
	cin >> StoreName;
	
	//Search StoreName in vector of STORES of the center:
	
	int Sfound = 0;
	int i = 0;
	int stpos = -1;
	while((Sfound == 0) && (i<mall.getSTORES().size())){
		if(strcasecmp(mall.getSTORES()[i].getStName().c_str(), StoreName.c_str()) == 0){
			Sfound = 1;
			stpos = i;
		}else{
			i++;
		}
	}
	
	
	if (stpos>=0){ //If store introduced by the user is found, then:
		cout << "\nIntroduce the NAME of the PRODUCT you want to add: ";
		cin >> ProdName;
		
		ProdName[0] = toupper(ProdName[0]); // upper case to first character of ProdName (cin) and with the 'for' of below:
											// lower case to the other characters so that all words follow the same format 
											// in ShowAllInfo and in the Output file :)
		
		for (int c = 1; c < ProdName.size(); c++){
			ProdName[c] = tolower(ProdName[c]);
		}
		
		//Search ProdName in Catalogue of its store:
		
		int Nfound = 0;
		int k = 0;
		int namepos = -1;
		while((Nfound == 0) && (k<mall.getSTORES()[stpos].getCatalogue().size())){
			if(strcasecmp(mall.getSTORES()[stpos].getCatalogue()[k].getProdName().c_str(), ProdName.c_str()) == 0){
				Nfound = 1;
				namepos = k;
			}else{
				k++;
			}
		}
		
		if (namepos >= 0){ //If  the NAME of the product introduced by the user is found in that store, then:
			cout << "\nThere is already a product with the same name. You must introduce a different ID:" << endl; //There can be more than one product with the same name, but they have to have different IDs!
		}
		
		cout << "\nIntroduce the ID of the PRODUCT you want to add: ";
		cin >> ProdID;
		cout << "\nIntroduce the PRICE of the PRODUCT you want to add: ";
		cin >> ProdPrice;
		
		//Search ProdID in Catalogue of its store:		
		int Pfound = 0;
		int j = 0;
		int prodpos = -1;
		while((Pfound == 0) && (j<mall.getSTORES()[stpos].getCatalogue().size())){
			if(mall.getSTORES()[stpos].getCatalogue()[j].getProdID() == ProdID){
				Pfound = 1;
				prodpos = j;
			}else{
				j++;
			}
		}
		if (prodpos>=0){ //If PRODUCT ID found on catalogue:
			cout << "\nProduct not added as it is already on Catalogue." << endl;
		}else{
			Product newProd(ProdName, ProdID, ProdPrice); 
			
			mall.setNewProd(stpos,newProd);
			
			cout << "\n\n'" << ProdName << "' has been added in " << mall.getSTORES()[stpos].getStName() << " with ID: " << ProdID << " and price: " << ProdPrice << " euros." << endl;
			
		}
		
	}else{
		cout << "\nStore not found. Try Again by choosing option 3 in the menu." << endl;
	}

}

void removeProductInStore(class Center &mall){
	//removes prod from a store's catalogue:
	//Ask store and prod ID
	//Check prod already exist in catalogue
	
	string StoreName, ProdID;
	cout << "Introduce the NAME of the STORE you want to search: ";
	cin >> StoreName;
	
	StoreName[0] = toupper(StoreName[0]); 
	
	for (int c = 1; c < StoreName.size(); c++){
		StoreName[c] = tolower(StoreName[c]);
	}
	
	//Search StoreName in vector of STORES of the center:
	
	int Sfound = 0;
	int i = 0;
	int stpos = -1;
	while((Sfound == 0) && (i<mall.getSTORES().size())){
		if(strcasecmp(mall.getSTORES()[i].getStName().c_str(), StoreName.c_str()) == 0){
			Sfound = 1;
			stpos = i;
		}else{
			i++;
		}
	}
	
	if (stpos>=0){ // If store found, then:
		
		cout << "\nIntroduce the ID of the product you want to search: ";
		cin >> ProdID;
	
		cout << "\nStore found. Searching Product..." << endl;
		int Pfound = 0;
		int j = 0;
		int prodpos = -1;
		while((Pfound == 0) && (j<mall.getSTORES()[stpos].getCatalogue().size())){
			if(mall.getSTORES()[stpos].getCatalogue()[j].getProdID() == ProdID){
				Pfound = 1;
				prodpos = j;
			}else{
				j++;
			}
		}
		if (prodpos>=0){ //If product found in its catalogue:
			mall.EraseProd(stpos,prodpos);
			cout << "\nThe product with ID: " << ProdID << " has been removed from " << StoreName << "'s catalogue." << endl;
		}else{ // If product user wants to remove is not found, then:
			cout << "\nProduct ID not found. Try Again by choosing option 4 in the menu" << endl;
		}
		
	}else{ // If store not found:
		cout << "\nStore not found. Try Again by choosing option 4 in the menu." << endl; 
	}
	
}

void showAllInformation(class Center mall){
	//prints all the info related to center, stores, employees, products.
	
		
	cout << "CENTER INFORMATION:" << endl;
	cout << "\nName: " << mall.getName() << endl;
	cout << "Adress: " << mall.getAdress() << endl;
	cout << "Number of parking slots: " << mall.getNpark() << endl;
	cout << "List of center employees:" << endl;
	

	for (int i = 0; i < mall.getCenterEmps().size(); i++){
		cout << "\nEmployee " << i + 1 << ":" << endl;
		cout << "Name: " << mall.getCenterEmps()[i].getEmpName() << endl;
		cout << "ID: " << mall.getCenterEmps()[i].getID() << endl;
		cout << "Adress: " << mall.getCenterEmps()[i].getEmpAdress() << endl;
		cout << "Telephone: " << mall.getCenterEmps()[i].getTelephone() << endl;
		cout << "Salary: " << mall.getCenterEmps()[i].getSalary() << endl;
		cout << "Occupation: " << mall.getCenterEmps()[i].getOccupation() << endl;
	}
	cout << "\nSTORES INFORMATION:" << endl;
	for (int j = 0; j < mall.getSTORES().size(); j++){
		cout << "\nStore " << j+1 << ":" << endl;
		cout << "Name: " << mall.getSTORES()[j].getStName() << endl;
		cout << "ID: " << mall.getSTORES()[j].getStoreID() << endl;
		cout << "Area: " << mall.getSTORES()[j].getArea() << endl;  
		cout << "Status: " << mall.getSTORES()[j].getStatus() << endl;
		for (int k = 0; k < mall.getSTORES()[j].getStEmps().size(); k++){
			cout << "\nEmployee " << k+1 << ":" << endl;
			cout << "Name: " << mall.getSTORES()[j].getStEmps()[k].getEmpName() << endl;
			cout << "ID: " << mall.getSTORES()[j].getStEmps()[k].getID() << endl;
			cout << "Adress: " << mall.getSTORES()[j].getStEmps()[k].getEmpAdress() << endl;
			cout << "Telephone: " << mall.getSTORES()[j].getStEmps()[k].getTelephone() << endl;
			cout << "Salary: " << mall.getSTORES()[j].getStEmps()[k].getSalary() << endl;
			cout << "Associated Status: " << mall.getSTORES()[j].getStEmps()[k].getAssociatedStatus() << endl;
		}
		for (int l = 0; l < mall.getSTORES()[j].getCatalogue().size(); l++){
			cout << "\nProduct " << l+1 << ":" << endl;
			cout << "Name: " << mall.getSTORES()[j].getCatalogue()[l].getProdName() << endl;
			cout << "ID: " << mall.getSTORES()[j].getCatalogue()[l].getProdID() << endl;
			cout << "Price: " << mall.getSTORES()[j].getCatalogue()[l].getPrice() << " euros" << endl;
		}
	}
	
}

void saveAllInformation(class Center mall){
	//all the info related to ctr, strs, emps, prods stored in a text file: 'Output.txt'
	
	ofstream ofile("Output.txt"); 

	if(ofile.fail()){
		cout << "Error while opening Output file" << endl;
	}else{
		
		ofile << "CENTER INFORMATION:" << endl;
		ofile << "\nName: " << mall.getName() << endl;
		ofile << "Adress: " << mall.getAdress() << endl;
		ofile << "Number of parking slots: " << mall.getNpark() << endl;
		ofile << "List of center employees:" << endl;
	
		for (int i = 0; i < mall.getCenterEmps().size(); i++){
			ofile << "\nEmployee " << i + 1 << ":" << endl;
			ofile << "Name: " << mall.getCenterEmps()[i].getEmpName() << endl;
			ofile << "ID: " << mall.getCenterEmps()[i].getID() << endl;
			ofile << "Adress: " << mall.getCenterEmps()[i].getEmpAdress() << endl;
			ofile << "Telephone: " << mall.getCenterEmps()[i].getTelephone() << endl;
			ofile << "Salary: " << mall.getCenterEmps()[i].getSalary() << endl;
			ofile << "Occupation: " << mall.getCenterEmps()[i].getOccupation() << endl;
		}
		ofile << "\nSTORES INFORMATION:" << endl;
		for (int j = 0; j < mall.getSTORES().size(); j++){
			ofile << "\nStore " << j+1 << ":" << endl;
			ofile << "Name: " << mall.getSTORES()[j].getStName() << endl;
			ofile << "ID: " << mall.getSTORES()[j].getStoreID() << endl;
			ofile << "Area: " << mall.getSTORES()[j].getArea() << endl;  
			ofile << "Status: " << mall.getSTORES()[j].getStatus() << endl;
			for (int k = 0; k < mall.getSTORES()[j].getStEmps().size(); k++){
				ofile << "\nEmployee " << k+1 << ":" << endl;
				ofile << "Name: " << mall.getSTORES()[j].getStEmps()[k].getEmpName() << endl;
				ofile << "ID: " << mall.getSTORES()[j].getStEmps()[k].getID() << endl;
				ofile << "Adress: " << mall.getSTORES()[j].getStEmps()[k].getEmpAdress() << endl;
				ofile << "Telephone: " << mall.getSTORES()[j].getStEmps()[k].getTelephone() << endl;
				ofile << "Salary: " << mall.getSTORES()[j].getStEmps()[k].getSalary() << endl;
				ofile << "Associated Status: " << mall.getSTORES()[j].getStEmps()[k].getAssociatedStatus() << endl;
			}
			for (int l = 0; l < mall.getSTORES()[j].getCatalogue().size(); l++){
				ofile << "\nProduct " << l+1 << ":" << endl;
				ofile << "Name: " << mall.getSTORES()[j].getCatalogue()[l].getProdName() << endl;
				ofile << "ID: " << mall.getSTORES()[j].getCatalogue()[l].getProdID() << endl;
				ofile << "Price: " << mall.getSTORES()[j].getCatalogue()[l].getPrice() << " euros" << endl;
			}
		}
		
		//After code:
		cout << "All information has been saved in Output.txt file correctly!" << endl;
	}
	ofile.close();
	
}

