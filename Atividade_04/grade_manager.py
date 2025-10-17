def register_grades():
    students = []
    grades = []
    
    print("=== REGISTRO DE NOTAS ===")
    print("Digite as notas dos alunos (digite 'fim' para encerrar)")
    
    while True:
        student_name = input("\nNome do aluno (ou 'fim' para encerrar): ")
        
        if student_name.lower() == 'fim':
            break
            
        try:
            grade = float(input(f"Nota do(a) {student_name}: "))
            
            if 0 <= grade <= 10:
                students.append(student_name)
                grades.append(grade)
                print(f"Nota de {student_name} registrada: {grade}")
            else:
                print("Erro: A nota deve estar entre 0 e 10!")
                
        except ValueError:
            print("Erro: Digite uma nota válida!")
    
    if grades:
        class_average = sum(grades) / len(grades)
        
        print("\n" + "="*40)
        print("RELATÓRIO DA TURMA")
        print("="*40)
        print(f"Total de alunos: {len(students)}")
        print(f"Média da turma: {class_average:.2f}")
        
        print("\nNotas individuais:")
        for i, (student, grade) in enumerate(zip(students, grades), 1):
            status = "Aprovado" if grade >= 7.0 else "Reprovado"
            print(f"{i}. {student}: {grade} - {status}")
        
        print(f"\nEstatísticas:")
        print(f"Maior nota: {max(grades)}")
        print(f"Menor nota: {min(grades)}")
        print(f"Alunos aprovados: {len([g for g in grades if g >= 7.0])}")
        print(f"Alunos reprovados: {len([g for g in grades if g < 7.0])}")
        
    else:
        print("Nenhuma nota foi registrada!")

if __name__ == "__main__":
    register_grades()