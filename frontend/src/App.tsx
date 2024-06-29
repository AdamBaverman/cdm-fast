import React, { useEffect, useState } from 'react';
import axios from 'axios';
import {
  Container,
  Typography,
  TextField,
  Button,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
} from '@mui/material';

interface Character {
  id?: string;
  full_name: string;
  age: number;
  gender: string;
}

const App: React.FC = () => {
  const [characters, setCharacters] = useState<Character[]>([]);
  const [fullName, setFullName] = useState('');
  const [age, setAge] = useState<number | string>('');
  const [gender, setGender] = useState('');
  const [editingCharacter, setEditingCharacter] = useState<Character | null>(null);

  useEffect(() => {
    fetchCharacters();
  }, []);

  const fetchCharacters = async () => {
    try {
      const response = await axios.get(`${process.env.REACT_APP_API_URL}/characters`); // .env файл должен находится в корневой директории проекта frontend, а не в frontend/src
      setCharacters(response.data);
    } catch (error) {
      console.error('Error fetching characters:', error);
    }
  };

  const handleAddCharacter = async () => {
    try {
      const newCharacter: Character = { full_name: fullName, age: Number(age), gender };
      await axios.post(`${process.env.REACT_APP_API_URL}/characters`, newCharacter);
      setFullName('');
      setAge('');
      setGender('');
      fetchCharacters();
    } catch (error) {
      console.error('Error adding character:', error);
    }
  };

  const handleUpdateCharacter = async () => {
    if (!editingCharacter) return;
    try {
      const updatedCharacter: Character = { full_name: fullName, age: Number(age), gender };
      await axios.put(`${process.env.REACT_APP_API_URL}/characters/${editingCharacter.id}`, updatedCharacter);
      setEditingCharacter(null);
      setFullName('');
      setAge('');
      setGender('');
      fetchCharacters();
    } catch (error) {
      console.error('Error updating character:', error);
    }
  };

  const handleEditCharacter = (character: Character) => {
    setEditingCharacter(character);
    setFullName(character.full_name);
    setAge(character.age);
    setGender(character.gender);
  };

  const handleDeleteCharacter = async (id?: string) => {
    if (!id) return;
    try {
      await axios.delete(`${process.env.REACT_APP_API_URL}/characters/${id}`);
      fetchCharacters();
    } catch (error) {
      console.error('Error deleting character:', error);
    }
  };

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Fantasy World Characters
      </Typography>
      <TextField
        label="Full Name"
        value={fullName}
        onChange={(e) => setFullName(e.target.value)}
        fullWidth
        margin="normal"
      />
      <TextField
        label="Age"
        value={age}
        onChange={(e) => setAge(e.target.value)}
        fullWidth
        margin="normal"
        type="number"
      />
      <TextField
        label="Gender"
        value={gender}
        onChange={(e) => setGender(e.target.value)}
        fullWidth
        margin="normal"
      />
      {editingCharacter ? (
        <Button variant="contained" color="primary" onClick={handleUpdateCharacter}>
          Update Character
        </Button>
      ) : (
        <Button variant="contained" color="primary" onClick={handleAddCharacter}>
          Add Character
        </Button>
      )}
      <TableContainer component={Paper} style={{ marginTop: '20px' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Full Name</TableCell>
              <TableCell>Age</TableCell>
              <TableCell>Gender</TableCell>
              <TableCell>Actions</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {characters.map((character) => (
              <TableRow key={character.id}>
                <TableCell>{character.full_name}</TableCell>
                <TableCell>{character.age}</TableCell>
                <TableCell>{character.gender}</TableCell>
                <TableCell>
                  <Button variant="contained" color="secondary" onClick={() => handleEditCharacter(character)}>
                    Edit
                  </Button>
                  <Button variant="contained" color="error" onClick={() => handleDeleteCharacter(character.id)}>
                    Delete
                  </Button>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Container>
  );
};

export default App;
