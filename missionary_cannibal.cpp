#include<bits/stdc++.h>
#define st pair< int , pair< pair<int,int> , pair<int,int> > >
using namespace std ;
//left ->0 and right -> 1
map< st  , st >parent ;
int isgoal( st state ){
	if( state.second.first.first == 0 && state.second.first.second == 0 ){
		return 1 ;
	}
	return 0 ;
}

int isvalid( st state ){
	int cannleft = state.second.first.first ;
	int missleft = state.second.first.second ;
	int cannright = state.second.second.first ;
	int missright = state.second.second.second ;
	
	if( cannleft >= 0 && missleft >= 0 && cannright >= 0 && missright >= 0 && 
		( missleft == 0 || missleft >= cannleft ) && ( missright == 0 || missright >= cannright ) ){
		return true ;		
	}
	return false ;
}
void testandADD( vector< st > &succ  , st state , st par ){
	if( isvalid( state ) ){
	//	cout<<"test\n" ;
		succ.push_back( state ) ;
	//	parent[state] = par ;
	}
}
vector< st > generate_successor( st state ){
	vector< st >succ ;
	int cannleft = state.second.first.first ;
	int missleft = state.second.first.second ;
	int cannright = state.second.second.first ;
	int missright = state.second.second.second ;
	//cout<<"succe\n" ;
	if( state.first == 0 ){
		testandADD( succ , make_pair(1,make_pair(make_pair(cannleft-2,missleft),make_pair(cannright+2,missright))),state) ;
		testandADD( succ , make_pair(1,make_pair(make_pair(cannleft,missleft-2),make_pair(cannright,missright+2))),state) ;
		testandADD( succ , make_pair(1,make_pair(make_pair(cannleft-1,missleft-1),make_pair(cannright+1,missright+1))),state);
		testandADD( succ , make_pair(1,make_pair(make_pair(cannleft-1,missleft),make_pair(cannright+1,missright))),state) ;
		testandADD( succ , make_pair(1,make_pair(make_pair(cannleft,missleft-1),make_pair(cannright,missright+1))),state) ;
	}
	else{
		testandADD( succ , make_pair(0,make_pair(make_pair(cannleft+2,missleft),make_pair(cannright-2,missright))),state) ;
		testandADD( succ , make_pair(0,make_pair(make_pair(cannleft,missleft+2),make_pair(cannright,missright-2))),state) ;
		testandADD( succ , make_pair(0,make_pair(make_pair(cannleft+1,missleft+1),make_pair(cannright-1,missright-1))),state) ;
		testandADD( succ , make_pair(0,make_pair(make_pair(cannleft+1,missleft),make_pair(cannright-1,missright))),state) ;
		testandADD( succ , make_pair(0,make_pair(make_pair(cannleft,missleft+1),make_pair(cannright,missright-1))),state) ;
	}
	return succ ;
}
st executeBFS( st initialstate ){
	if( isgoal( initialstate ) ){
		return initialstate ;
	}
	
	queue< st >que ;
	map< st , int >map1 ;
	
	//cout<<"executebfs\n" ;
	que.push( initialstate ) ;
	map1[initialstate] = 1 ;
	while( !que.empty() ){
		st state = que.front() ;
		que.pop() ;
		vector< st >succ ;
	//	cout<<"que\n" ;
		succ = generate_successor( state ) ;
	//	cout<<succ.size()<<"\n" ;
		for( int i = 0 ; i < succ.size() ; i++ ){
			st child = succ[i] ;
			if( map1.find(child) == map1.end() ){
				map1[child] = 1 ;
				parent[child] = state ;
				if( isgoal(child) ){
					return child ;
				}
				que.push( child ) ;
			}
		}
	}
}

void printsolution( st solution ){
	cout<<"Solution (cannibalLeft,missionaryLeft,boat,cannibalRight,missionaryRight): \n";
	vector< st >path ;
	
	while( 1 ){
		if( parent[solution] == solution ){
			break ;
		}
		path.push_back( solution ) ;
		solution = parent[solution] ;
	}
	path.push_back( solution ) ;
	int sz = path.size() ;
	for( int i = sz-1 ; i >= 0 ; i-- ){
		cout<<path[i].second.first.first<<" "<<path[i].second.first.second<<" -> ";
		if( path[i].first == 0 )
			cout<<" LEFT -> ";
		else
			cout<<" RIGHT -> "; 
		cout<<path[i].second.second.first<<" "<<path[i].second.second.second<<"\n" ;
	}
	//cout<<"aihs\n" ;
	
}
int main(){
	cout<<"<----Missionaries and Cannibals Problem---->\n" ;
	
	st initialstate = make_pair(0,make_pair(make_pair(3,3),make_pair(0,0))) ;
	parent[initialstate] = initialstate ;
	st solution = executeBFS( initialstate ) ;
	printsolution( solution ) ;
	
}
