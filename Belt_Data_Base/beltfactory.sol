pragma  solidity  ^0.4.25;

contract Beltfactory {
    
    event NewAthlete(uint256 id, string name, uint256 birthdate, uint256 firstTrainingDate, uint8 belt, uint256[] promotionsDate);
    
    struct Athlete {
	    string name;
	    uint256 birthdate;
	    uint256 firstTrainingDate;
	    uint8 belt;
	    uint256 id;
	}
	
	uint256[] promotionsDate;
	
	Athlete[] public athletes;
	
	
	
	mapping (address => Athlete) public addressToAthletes;
	mapping (uint => address) public athleteToId;
	mapping (address => uint256[]) public addressToPromotionsDate;
	
	//Função para cadastrar atleta
    function addAthlete(string _name, uint256 _birthdate, uint256 _firstTrainingDate) public {
        
        
        uint _athleteId = athletes.push(Athlete(_name, _birthdate, _firstTrainingDate, 0, _athleteId)) - 1;
        
        addressToPromotionsDate[msg.sender].push(_firstTrainingDate);
        addressToAthletes[msg.sender] = athletes[_athleteId];
        athleteToId[_athleteId] = msg.sender;
        
        
        emit NewAthlete(_athleteId, _name, _birthdate, _firstTrainingDate, 0,addressToPromotionsDate[msg.sender]);
        
    }
    
    
    //Função para ver atleta
    function getAthlete(address _athleteAdress) public view returns (uint256 id, string name, uint256 birthdate, uint256 firstTrainingDate, uint8 belt, uint256[] promotionsDate) {
        return (
            addressToAthletes[_athleteAdress].id,
            addressToAthletes[_athleteAdress].name,
            addressToAthletes[_athleteAdress].birthdate,
            addressToAthletes[_athleteAdress].firstTrainingDate,
            addressToAthletes[_athleteAdress].belt,
            addressToPromotionsDate[_athleteAdress]
            );
        
    }

    //Função para ver atleta por Id
    function getAthleteById(uint _athleteId) public view returns (string name, uint256 birthdate, uint256 firstTrainingDate, uint8 belt, uint256[] promotionsDate) {
        return (
            addressToAthletes[ athleteToId[_athleteId]].name,
            addressToAthletes[ athleteToId[_athleteId]].birthdate,
            addressToAthletes[ athleteToId[_athleteId]].firstTrainingDate,
            addressToAthletes[ athleteToId[_athleteId]].belt,
            addressToPromotionsDate[ athleteToId[_athleteId]]
            );
        
    }
    

}


 /*
        
        var storage athlete = addressToAthletes[msg.sender];
        
        athlete.name = _name;
        athlete.birthdate = _birthdate;
        athlete.firstTrainingDate = _firstTrainingDate;
        athlete.belt = 0;
        athlete.promotionsDate.push(_fisrtTrainingDate);
        
        athletes.push(athletesAddress) -1;
        
        */
        
        
        //address[] public athletesAddress;