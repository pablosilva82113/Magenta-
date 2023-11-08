import React, { Component } from 'react';
import './Board.css';

class Board extends Component {
    constructor(props) {
        super(props);
        this.state = {
            board: [
                ['L', 'L', 'L', 'L', 'L', 'X', 'L', 'L'],
                ['L', 'L', 'L', 'L', 'L', 'X', 'L', 'L'],
                ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L'],
                ['L', 'L', 'L', 'L', 'L', 'X', 'L', 'L'],
                ['L', 'L', 'L', 'L', 'L', 'X', 'L', 'L'],
                ['L', 'L', 'L', 'L', 'L', 'X', 'L', 'B'],
            ],
            positionX: 0,
            positionY: 0,
            currentIndex: 0,
            isExecutingInstructions: false,
            instructions: [],
        };
    }

    loadInstructionsFromAPI = () => {
        this.setState({ isExecutingInstructions: true });

        fetch('http://127.0.0.1:8000/ejecutar_instrucciones')
            .then((response) => response.json())
            .then((data) => {
                const instructions = data.resultado;

                if (Array.isArray(instructions) && instructions.length > 0) {
                    this.setState({ instructions }, () => {
                        this.processInstructions();
                    });
                } else {
                    console.error('Los datos de la API no son válidos.');
                }
            })
            .catch((error) => {
                console.error('Error al obtener los datos de la API: ', error);
            });
    };

    processInstructions = () => {
        const { instructions, currentIndex } = this.state;
        if (currentIndex < instructions.length) {
            const instruction = instructions[currentIndex];
            this.setState(
                {
                    positionX: instruction['Pos X'],
                    positionY: instruction['Pos Y'],
                    currentIndex: currentIndex + 1,
                },
                () => {
                    setTimeout(this.processInstructions, 250);
                }
            );
        } else {
            this.setState({ isExecutingInstructions: false });
        }
    };
    getCellClassName = (cell, rowIndex, columnIndex) => {
        if (cell === 'B') {
            return 'cell-red';
        }
        if (cell === 'X') {
            return 'cell-blue';
        }
        return rowIndex === this.state.positionY && columnIndex === this.state.positionX
            ? 'active'
            : '';
    };

    render() {
        const { board, positionX, positionY } = this.state;
        return (
            <div className="container text-center">
                <table className="board">
                    <tbody>
                    {board.map((row, rowIndex) => (
                        <tr key={rowIndex}>
                            {row.map((cell, columnIndex) => (
                                <td
                                    key={columnIndex}
                                    className={this.getCellClassName(cell, rowIndex, columnIndex)}
                                >
                                    {rowIndex === positionY && columnIndex === positionX ? (
                                        <span className="material-symbols-outlined">robot_2</span>
                                    ) : (
                                        cell
                                    )}
                                </td>
                            ))}
                        </tr>
                    ))}
                    </tbody>
                </table>
                <button
                    type="button"
                    className="btn btn-success mt-2"
                    onClick={this.loadInstructionsFromAPI}
                    disabled={this.state.isExecutingInstructions}>
                    Ejecutar Instrucciones
                </button>

            </div>
        );
    }
}

export default Board;


