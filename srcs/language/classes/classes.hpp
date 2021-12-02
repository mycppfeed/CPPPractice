class EmptyClass { };

class SimpleClass_0 {
    public:
        int x = 0;
};

class SimpleClass_1 {
    private:
        int _x = 0;
    public:
        void setX(int x) { _x = x; }
        int getX() { return _x; }
};