pragma  solidity  ^0.4.25;

import "./beltfactory.sol";

contract  Beltdb is Beltfactory{
    
    address founder;
    
    constructor() public {
		founder =  msg.sender;
	}
	

	modifier blackBeltOnly {
	    require(addressToAthletes[msg.sender].belt > 3, "Only black belts can invoke this function");//WARNING HERE!!!!!!!
	    _;
	}
	
	modifier founderOnly {
	   require(msg.sender == founder, "Only founder can invoke this function");
	    _;
	}


    
    //Função para promover atleta, bb olnly
    function promoteAthlete(address _athleteAddress) public blackBeltOnly {
        if (addressToAthletes[msg.sender].belt > addressToAthletes[_athleteAddress].belt + 1) {
            addressToAthletes[_athleteAddress].belt++;
            addressToPromotionsDate[_athleteAddress].push(now);
        }
        
    }
    
    
    
    
    //Função para editar atletas
    function editAthete(address _athleteAddress, uint8 _belt) public founderOnly {
        addressToAthletes[_athleteAddress].belt = _belt;
    }
    

    
}