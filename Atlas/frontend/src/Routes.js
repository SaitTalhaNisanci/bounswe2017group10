import { connect } from 'react-redux';
import axios from 'axios';
import Routes from './components/Routes';
import { updateUser } from './actions/index';

const mapStateToProps = state => {
  return {
    token: state.token
  };
}

const mapDispatchToProps = dispatch => {
  return {
    fetchUser: () => {
      axios.get('localhost:8000/api/auth/me')
        .then(data => {
           dispatch(updateUser(data.response.data));
        })
        .catch(err => {
          console.log(err.response.data)
        });
    }
  };
}

const RoutesContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(Routes);

export default RoutesContainer;